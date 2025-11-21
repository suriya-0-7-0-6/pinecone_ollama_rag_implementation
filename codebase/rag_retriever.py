import os
import json
import hashlib
import time
import requests
import numpy as np
from typing import List, Dict, Tuple, Optional
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

# try:
#     from sentence_transformers import CrossEncoder
#     CROSS_ENCODER_AVAILABLE = True
# except Exception:
#     CROSS_ENCODER_AVAILABLE = False

# try:
#     from rank_bm25 import BM25Okapi
#     BM25_AVAILABLE = True
# except Exception:
#     BM25_AVAILABLE = False

load_dotenv()

def get_environmental_variables():

    ENVS = {
        "PINECONE_API_KEY": os.getenv('PINECONE_API_KEY'),
        "PINECONE_INDEX": os.getenv('PINECONE_INDEX'),
        "PINECONE_REGION": os.getenv('PINECONE_REGION'),
        "EMBEDDING_MODEL_NAME": os.getenv('EMBEDDING_MODEL_NAME', 'all-MiniLM-L6-v2'),
        "MAPPING_FILE": os.getenv('MAPPING_FILE', 'id_to_text_map.json'),
        "OLLAMA_URL": os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat"),
        "N_CANDIDATES": int(os.getenv('N_CANDIDATES', '20')),
        "TOP_K_TO_RETURN": int(os.getenv('TOP_K_TO_RETURN', '3')),
        "SCORE_THRESHOLD": float(os.getenv('SCORE_THRESHOLD', '0.20')),
        "CACHE_PATH": os.getenv('QUERY_CACHE_PATH', 'query_cache.json'),
        "RERANKER_MODEL": os.getenv('RERANKER_MODEL', 'cross-encoder/ms-marco-MiniLM-L-6-v2'),
        "CROSS_ENCODER_AVAILABLE": os.getenv('CROSS_ENCODER_AVAILABLE', True),
        "BM25_AVAILABLE": os.getenv('BM25_AVAILABLE', True),
        "USE_HYBRID": os.getenv('USE_HYBRID', 'true').lower() in ('1', 'true', 'yes'),
        "DEFAULT_NAMESPACE": os.getenv('DEFAULT_NAMESPACE', 'my_corpus'),
        "NAMESPACE_FILE": os.getenv('NAMESPACE_FILE', 'namespaces.json'),
        "MONITORING_FILE": os.getenv('MONITORING_FILE', 'monitoring_logs.jsonl'),
    }
    return ENVS
ENVS = get_environmental_variables()


print("\n🔧 Loaded environment:")
print(f"  Pinecone Index: {ENVS['PINECONE_INDEX']}")
print(f"  Ollama URL: {ENVS['OLLAMA_URL']}")
print(f"  Embedding model: {ENVS['EMBEDDING_MODEL_NAME']}")
print(f"  Reranker available: {ENVS['CROSS_ENCODER_AVAILABLE']}, BM25 available: {ENVS['BM25_AVAILABLE']}")
print(f"  Hybrid enabled: {ENVS['USE_HYBRID']}\n")

pc = Pinecone(api_key=ENVS["PINECONE_API_KEY"])
index = pc.Index(ENVS["PINECONE_INDEX"])
model = SentenceTransformer(ENVS["EMBEDDING_MODEL_NAME"])


def check_if_reranker_available():
    if ENVS["CROSS_ENCODER_AVAILABLE"]:
        try:
            from sentence_transformers import CrossEncoder
            RERANKER = CrossEncoder(ENVS["RERANKER_MODEL"])
            print(f"Cross-encode loaded: {ENVS['RERANKER_MODEL']}")
        except Exception as e:
            print(f"Failed to load cross-encode {ENVS['RERANKER_MODEL']}: {e}")
            RERANKER = None
    return RERANKER
RERANKER = check_if_reranker_available()

def load_query_cache():
    try:
        if os.path.exists(["CACHE_PATH"]):
            with open(ENVS["CACHE_PATH"], 'r', encoding='utf-8') as f:
                QUERY_CACHE = json.load(f)
        else:
            QUERY_CACHE = {}
        return QUERY_CACHE
    except Exception:
        QUERY_CACHE = {}
        return QUERY_CACHE
QUERY_CACHE = load_query_cache()


def load_namespace_config():
    namespace_configs = {}
    if os.path.exists(ENVS["NAMESPACE_FILE"]):
        with open(ENVS["NAMESPACE_FILE"], 'r') as f:
            namespace_configs = json.load(f)
    else:
        namespace_configs = {
            'active_namespace': ENVS["DEFAULT_NAMESPACE"],
            'allowed_namespaces': [ENVS["DEFAULT_NAMESPACE"]]
        }
    return namespace_configs
NAMESPACE_CONFIG = load_namespace_config()


def get_active_namespace():
    print(f"Active Namespace set to: {NAMESPACE_CONFIG.get('active_namespace', ENVS['DEFAULT_NAMESPACE'])}")
    return NAMESPACE_CONFIG.get("active_namespace", ENVS["DEFAULT_NAMESPACE"])


def set_namespace(namespace: str):
    if namespace not in NAMESPACE_CONFIG['allowed_namespaces']:
        NAMESPACE_CONFIG['allowed_namespaces'].append(namespace)
    NAMESPACE_CONFIG['active_namespace'] = namespace
    with open(ENVS["NAMESPACE_FILE"], 'w') as f:
        json.dump(NAMESPACE_CONFIG, f, indent=2)
    print(f"🌐 Active namespace set to: {namespace}")


def get_data(mapping_file, bm25_available):
    id_to_text = {}
    doc_ids_ordered = []
    doc_texts_ordered = []
    doc_tokens_ordered = []
    if os.path.exists(mapping_file):
        with open(mapping_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                    cid = item.get("id")
                    text = item.get("text")
                    if cid:
                        id_to_text[cid] = {"text": text, "metadata": item.get("metadata", {})}
                        doc_ids_ordered.append(cid)
                        doc_texts_ordered.append(text)
                        if bm25_available:
                            tokens = text.lower().split()
                            doc_tokens_ordered.append(tokens)
                except Exception:
                    continue
        print(f"📂 Loaded mapping for {len(id_to_text)} chunks from {mapping_file}")
        return id_to_text, doc_ids_ordered, doc_texts_ordered, doc_tokens_ordered
    else:
        print(f"⚠️ Mapping file '{ENVS['MAPPING_FILE']}' not found. Retrieval will still use metadata if present in Pinecone.")
        return id_to_text, doc_ids_ordered, doc_texts_ordered, doc_tokens_ordered
id_to_text, doc_ids_ordered, doc_texts_ordered, doc_tokens_ordered = get_data(ENVS["MAPPING_FILE"], ENVS["BM25_AVAILABLE"])


def check_if_bm25_availability_and_build_index():
    if ENVS["BM25_AVAILABLE"] and ENVS["USE_HYBRID"] and len(doc_tokens_ordered) > 0:
        from rank_bm25 import BM25Okapi
        bm25 = BM25Okapi(doc_tokens_ordered)
        print("✅ BM25 index built for hybrid retrieval.")
        return bm25
    else:
        print("BM25 not available. Skipping hybrid search!")
        return None
bm25 = check_if_bm25_availability_and_build_index()


def log_event(event: Dict, MONITORING_FILE: str = ENVS["MONITORING_FILE"]):
    event['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(MONITORING_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def save_cache():
    with open(ENVS["CACHE_PATH"], "w", encoding="utf-8") as f:
        json.dump(QUERY_CACHE, f, ensure_ascii=False, indent=2)
    

def cache_key_for(query:str, metadata_filter: Optional[Dict]=None, namespace: str = None) -> str:
    key_obj = {"q": query, "filter": metadata_filter, "namespace": namespace or get_active_namespace()}
    key_str = json.dumps(key_obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(key_str.encode()).hexdigest()


def l2_normalize(vec):
    """Return vector normalized to unit length"""
    vec = np.array(vec)
    return (vec / (np.linalg.norm(vec) + 1e-10)).tolist()


def generate_query_embedding(query_text: str) -> List[float]:
    print(f"\n🧠 Generating embedding for query: '{query_text}'")
    query_embedding = model.encode([query_text])[0]
    query_embedding = l2_normalize(query_embedding)
    print(f"✅ Embedding dimension: {len(query_embedding)}")
    return query_embedding


def apply_metadata_filter(results: dict, metadata_filter: Optional[Dict]) -> List[dict]:
    if not metadata_filter:
        return results.get("matches", [])

    filtered = []
    for m in results.get("matches", []):
        meta = m.get("metadata", {}) or {}
        ok = True
        for k, v in metadata_filter.items():
            if isinstance(v, dict):
                continue
            if meta.get(k) != v:
                ok = False
                break
        if ok:
            filtered.append(m)
    return filtered


def get_bm25_score_for_cid(cid: str, query:str) -> float:
    if not (ENVS["BM25_AVAILABLE"] and bm25):
        return 0.0
    try:
        idx = doc_ids_ordered.index(cid)
        tokens = query.lower().split()
        scores = bm25.get_scores(tokens)
        raw = float(scores[idx])
        return raw
    except ValueError:
        return 0.0


def normalize_scores(values: List[float]) -> List[float]:
    arr = np.array(values, dtype=float)
    if len(arr) == 0:
        return []
    minv, maxv = arr.min(), arr.max()
    if maxv - minv <= 1e-12:
        return [1.0 for _ in arr]
    norm = (arr - minv) / (maxv - minv)
    return norm.tolist()


def retrieve_candidates(query_embedding: List[float], query_text: str, top_k: int = 5, metadata_filter: Optional[Dict] = None, min_score: float = ENVS["SCORE_THRESHOLD"]) -> List[Tuple[str, float]]:
    namespace = get_active_namespace()
    print(f"\n🔍 Querying namespace: {namespace}")
    pinecone_filter = metadata_filter if metadata_filter else None
    print(f"\n🔍 Querying Pinecone (top {ENVS['N_CANDIDATES']}) — applying server-side filter: {bool(pinecone_filter)}")
    res = index.query(
        vector=query_embedding,
        top_k=ENVS["N_CANDIDATES"],
        include_metadata=True,
        filter=pinecone_filter,
        namespace=namespace
    )
    matches = res.get("matches", [])
    print(f"  → Pinecone returned {len(matches)} matches")

    if len(matches) == 0:
        return []

    candidate_ids = []
    candidate_texts = []
    vector_scores = []
    for match in matches:
        cid = match.get("id")
        text = match.get("metadata", {}).get("text") or id_to_text.get(cid, {}).get("text", "")
        score = float(match.get("score", 0.0))
        candidate_ids.append(cid)
        candidate_texts.append(text)
        vector_scores.append(score)

    hybrid_scores = []
    if ENVS["USE_HYBRID"] and ENVS["BM25_AVAILABLE"]:
        bm25_raw = [get_bm25_score_for_cid(cid, query_text) for cid in candidate_ids]
        bm25_norm = normalize_scores(bm25_raw)
        alpha = 0.75
        hybrid_scores = [alpha * vs + (1 - alpha) * bm for vs, bm in zip(vector_scores, bm25_norm)]
        print("  → Hybrid scores computed (vector + BM25)")
    else:
        hybrid_scores = vector_scores

    candidates = []
    for cid, text, vs, hs in zip(candidate_ids, candidate_texts, vector_scores, hybrid_scores):
        if hs >= min_score:
            candidates.append({
                "id": cid,
                "text": text,
                "vector_score": vs,
                "hybrid_score": hs
            })
    print(f"  → {len(candidates)} candidates remain after threshold >= {min_score}")
    if len(candidates) == 0:
        return []
        
    if RERANKER is not None:
        chunk_texts = [c["text"] for c in candidates]
        pairs = [[query_text, ct] for ct in chunk_texts]
        try:
            reranker_scores = RERANKER.predict(pairs)
            for c, r in zip(candidates, reranker_scores):
                c["rerank_score"] = float(r)
            candidates = sorted(candidates, key=lambda x: x["rerank_score"], reverse=True)
            print("  → Re-ranked candidates using Cross-Encoder.")
        except Exception as e:
            print(f"  ⚠️ Re-ranker failed: {e}. Falling back to hybrid scores.")
            candidates = sorted(candidates, key=lambda x: x["hybrid_score"], reverse=True)
    else:
        candidates = sorted(candidates, key=lambda x: x["hybrid_score"], reverse=True)
        print("  → Cross-encoder not available: sorted by hybrid scores.")
    
    top_candidates = [(c["text"], c.get("rerank_score", c["hybrid_score"])) for c in candidates[:top_k]]
    return top_candidates


def build_prompt(query_text: str, retrieved: List[Tuple[str, float]]) -> str:
    pieces = []
    for i, (chunk, score) in enumerate(retrieved):
        pieces.append(f"[{i+1}] (score: {score:.3f})\n{chunk}")
    context_text = "\n\n".join(pieces)
    prompt = f"""
    You are an AI assistant. Use ONLY the provided context snippets below to answer the user's question.
If the information is not present in the context, say "I couldn't find relevant information."

Context:
{context_text}

Question: {query_text}

Answer concisely, and include citations like [1], [2] referring to the context snippets above when you use them.
"""
    return prompt.strip()


def query_ollama(prompt: str, model_name: str = "gpt-oss:20b") -> str:
    print(f"\n⚡ Sending prompt to Ollama ({model_name}) — length {len(prompt)} chars")
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    response = requests.post(ENVS["OLLAMA_URL"], json=payload)
    response.raise_for_status()
    response_json = response.json()
    if "message" in response_json and "content" in response_json["message"]:
        return response_json["message"]["content"]
    if "response" in response_json:
        return response_json["response"]
    print("✅ Received response from Ollama.")
    return json.dumps(response_json)


def rag_pipeline(user_query: str, metadata_filter: Optional[Dict] = None, interactive_cache: bool = True) -> str:
    namespace = get_active_namespace()
    ck = cache_key_for(user_query, metadata_filter, namespace)
    if interactive_cache and ck in QUERY_CACHE:
        return QUERY_CACHE[ck]
    
    t0 = time.time()
    query_embedding = generate_query_embedding(user_query)
    candidates = retrieve_candidates(query_embedding, user_query, top_k=ENVS["TOP_K_TO_RETURN"], metadata_filter=metadata_filter)
    if not candidates:
        print("⚠️ No candidates found — relaxing threshold and retrying without metadata filter.")
        candidates = retrieve_candidates(query_embedding, user_query, top_k=ENVS["TOP_K_TO_RETURN"], metadata_filter=None, min_score=0.0)
        if not candidates:
            ans = "I couldn't find relevant information."
            QUERY_CACHE[ck] = ans
            save_cache()
            return ans

    prompt = build_prompt(user_query, candidates)
    answer = query_ollama(prompt)

    QUERY_CACHE[ck] = answer
    save_cache()
    dt = time.time() - t0
    print(f"\n✅ RAG complete (took {dt:.2f}s).")
    log_event({
        "query": user_query,
        "namespace": namespace,
        "used_cache": ck in QUERY_CACHE,
        "num_candidates": len(candidates),
        "metadata_filter": metadata_filter,
        "latency_seconds": round(dt, 3)
    })
    return answer


if __name__ == "__main__":
    print("\n🚀 RAG System Ready!")
    while True:
        user_query = input("\n🧾 Enter your question (or 'exit' to quit): ")
        if user_query.strip().lower() == "exit":
            print("👋 Exiting RAG assistant. Bye!!!")
            break
        metadata_filter = None
        if user_query.startswith("/filter"):
            try:
                _, rest = user_query.split(" ", 1)
                key, value = rest.split("=", 1)
                metadata_filter = {key.strip(): value.strip()}
                user_query = input("Enter query: ")
            except Exception:
                print("⚠️ Bad filter format. Use: /filter key=value.")
                continue
        else:
            user_query = user_query

        if user_query.startswith("/ns"):
            try:
                _, namespace = user_query.split(" ", 1)
                namespace = namespace.strip()
                set_namespace(namespace)
                continue
            except:
                print(f"⚠️ Usage: /ns {namespace}")
                continue

        answer = rag_pipeline(user_query, metadata_filter=metadata_filter)

        print("\n💬 Final Answer:\n")
        print(answer)
        print("\n" + "-" * 80)