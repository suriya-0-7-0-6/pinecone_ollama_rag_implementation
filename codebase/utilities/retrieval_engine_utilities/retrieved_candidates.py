# def retrieve_candidates(query_embedding, query_text, top_k, namespace="",  metadata_filter=None, min_score=ENVS["SCORE_THRESHOLD"]):
from utilities.normalize_vector import normalize_scores
from utilities.bm25_utils import get_bm25_score_for_cid

def retrieve_candidates(
        app_config,
        query_embedding,
        query_text,
        pinecone_index,
        namespace,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        metadata_filter,
        min_score=None
    ):
    print(f"\n🔍 Querying namespace: {namespace}")
    pinecone_filter = metadata_filter if metadata_filter else None
    print(f"\n🔍 Querying Pinecone (top {app_config.N_CANDIDATES}) — applying server-side filter: {bool(pinecone_filter)}")
    res = pinecone_index.query(
        vector=query_embedding,
        top_k=app_config.N_CANDIDATES,
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
    candidate_metadatas = []
    for match in matches:
        cid = match.get("id")
        text = match.get("metadata", {}).get("text") or id_to_text.get(cid, {}).get("text", "")
        metadata = match.get("metadata", {}) or id_to_text.get(cid, {}).get("metadata", {})
        score = float(match.get("score", 0.0))
        candidate_ids.append(cid)
        candidate_texts.append(text)
        vector_scores.append(score)
        candidate_metadatas.append(metadata)

    hybrid_scores = []
    if app_config.USE_HYBRID and app_config.BM25_AVAILABLE:
        bm25_raw = [get_bm25_score_for_cid(app_config, bm25, cid, query_text, docs_ids_ordered) for cid in candidate_ids]
        bm25_norm = normalize_scores(bm25_raw)
        alpha = 0.75
        hybrid_scores = [alpha * vs + (1 - alpha) * bm for vs, bm in zip(vector_scores, bm25_norm)]
        print("  → Hybrid scores computed (vector + BM25)")
    else:
        hybrid_scores = vector_scores

    candidates = []
    if min_score == None:
        min_score = 0.0
    
    for cid, text, metadata, vs, hs in zip(candidate_ids, candidate_texts, candidate_metadatas, vector_scores, hybrid_scores):
        if hs >= min_score:
            candidates.append({
                "id": cid,
                "text": text,
                "metadata": metadata,
                "vector_score": vs,
                "hybrid_score": hs
            })
    print(f"  → {len(candidates)} candidates remain after threshold >= {min_score}")
    if len(candidates) == 0:
        return []
        
    if reranker is not None:
        chunk_texts = [c["text"] for c in candidates]
        pairs = [[query_text, ct] for ct in chunk_texts]
        try:
            reranker_scores = reranker.predict(pairs)
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
    
    top_candidates = [(c["text"], c.get("rerank_score", c["hybrid_score"]), c["metadata"]) for c in candidates[:app_config.TOP_K_TO_RETURN]]
    
    return top_candidates