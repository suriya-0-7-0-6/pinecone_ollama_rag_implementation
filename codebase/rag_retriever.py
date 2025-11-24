import os
import json
import hashlib
import time
import sys
import requests
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from configs.get_envs import CONFIG
CONFIG.ensure_directories()

from utilities.load_query_cache import load_query_cache, save_query_cache, generate_256_hash_for_query
from utilities.load_namespace_config import load_namespace_config, set_namespace, get_active_namespace
from utilities.load_data import get_data_from_mapping_file
from utilities.normalize_vector import l2_normalizer
from utilities.load_reranker import load_reranker
from utilities.bm25_utils import check_if_bm25_availability_and_build_index
from utilities.log_events import log_event
from utilities.reasoning_engine_utilities.generate_query_embedding import  generate_query_embedding
from utilities.retrieval_engine_utilities.tiered_retriever import tiered_retriever
from utilities.retrieval_engine_utilities.retrieved_candidates import retrieve_candidates
from utilities.reasoning_engine_utilities.build_prompt import build_prompt
from utilities.reasoning_engine_utilities.query_ollama import query_ollama
from utilities.reasoning_engine_utilities.detect_hallucination import detect_hallucination
from utilities.reasoning_engine_utilities.compute_confidence import compute_confidence
from utilities.reasoning_engine_utilities.extract_citations import extract_citations
from utilities.retrieval_engine_utilities.format_response import format_response

def rag_pipeline(
        app_config,
        user_query, 
        pinecone_index, 
        namespace_config,
        query_cache,
        embedding_model,
        l2_normalizer,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        docs_texts_ordered,
        metadata_filter
    ):
    
    namespace = get_active_namespace(app_config, namespace_config)
    
    ck = generate_256_hash_for_query(user_query, metadata_filter, namespace)    
    
    used_cache = ck in query_cache
    if app_config and used_cache:
        log_event({"query": user_query, "used_cache": True}, app_config)
        return query_cache[ck]

    t0 = time.time()

    query_embedding = generate_query_embedding(user_query, embedding_model, l2_normalizer)

    retrieved_candidates, mode = tiered_retriever(
        app_config,
        query_embedding,
        user_query,
        pinecone_index,
        namespace,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        docs_texts_ordered,
        metadata_filter=metadata_filter
    )

    print(f"🔎 Retrieval mode used: {mode}")

    if not retrieved_candidates:
        print("⚠️ No candidates found — relaxing threshold and retrying without metadata filter.")
        retrieved_candidates = retrieve_candidates(
            app_config,
            query_embedding,
            user_query,
            pinecone_index,
            namespace,
            reranker,
            id_to_text, 
            docs_ids_ordered,
            metadata_filter=None,
        )
        if not retrieved_candidates:
            answer = "I couldn't find relevant information."
            query_cache[ck] = answer
            save_query_cache(app_config, query_cache)
            return answer

    prompt = build_prompt(user_query, retrieved_candidates)
    raw_response = query_ollama(app_config, prompt)
    cleaned_response = detect_hallucination(raw_response, retrieved_candidates)
    
    best_score = max((score for _, score, *_ in retrieved_candidates), default=0.0)
    extracted_citations = extract_citations(cleaned_response, retrieved_candidates)
    response_confidence = compute_confidence(best_score, len(retrieved_candidates), extracted_citations)
    
    cleaned_response += f"\n\n📊 **Answer Confidence:** {response_confidence}"

    query_cache[ck] = cleaned_response
    save_query_cache(app_config, query_cache)

    dt = time.time() - t0
    print(f"\n✅ RAG complete (took {dt:.2f}s).")

    log_event({
        "query": user_query,
        "namespace": namespace,
        "used_cache": used_cache,
        "num_candidates": len(retrieved_candidates),
        "metadata_filter": metadata_filter,
        "latency_seconds": round(dt, 3)
    }, app_config)

    if app_config.RAG_DEBUG:
        print("\n====== 🔍 RETRIEVAL DEBUG REPORT ======\n")
        print(f"Query: {user_query}")
        print(f"Namespace: {namespace}")
        print("\nRetrieved Candidates:")
        for i, (chunk, score, metadata) in enumerate(retrieved_candidates):
            print(f"[{i+1}] Score: {score:.3f}")
            print(chunk[:300] + "...\n")
        print("======================================\n")

    return format_response(
        app_config,
        cleaned_response,
        extracted_citations,
        response_confidence,
        mode,
        app_config.RAG_OUTPUT_STYLE
    )


if __name__ == "__main__":

    PINECONE = Pinecone(api_key=CONFIG.PINECONE_API_KEY)
    PINECONE_INDEX = PINECONE.Index(CONFIG.PINECONE_INDEX)
    EMBEDDING_MODEL = SentenceTransformer(CONFIG.EMBEDDING_MODEL_NAME)
    QUERY_CACHE = load_query_cache(CONFIG)
    NAMESPACE_CONFIG = load_namespace_config(CONFIG)
    ID_TO_TEXT, DOCS_IDS_ORDERED, DOCS_TEXTS_ORDERED, DOCS_TOKENS_ORDERED = get_data_from_mapping_file(CONFIG)    
    BM25 = check_if_bm25_availability_and_build_index(CONFIG, DOCS_TOKENS_ORDERED)
    RERANKER = load_reranker(CONFIG)

    print(f"ACTIVE NAMESPACE: {NAMESPACE_CONFIG['active_namespace']}")

    print("\n🚀 RAG System Ready!")

    while True:
        metadata_filter = None
        user_query = input("\n🧾 Enter your question (or 'exit' to quit): ")

        if user_query.strip().lower() == "exit":
            print("👋 Exiting RAG assistant. Bye!!!")
            break

        if user_query.startswith("/ns"):
            try:
                _, namespace = user_query.split(" ", 1)
                namespace = namespace.strip()
                set_namespace(namespace, CONFIG, NAMESPACE_CONFIG)
                continue
            except:
                print(f"Usage: /ns {namespace}")
                continue

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
        
        print(f"ACTIVE NAMESPACE: {NAMESPACE_CONFIG['active_namespace']}")

        answer = rag_pipeline(
            app_config=CONFIG,
            user_query=user_query, 
            pinecone_index=PINECONE_INDEX,
            namespace_config=NAMESPACE_CONFIG,
            query_cache=QUERY_CACHE,
            embedding_model=EMBEDDING_MODEL,
            l2_normalizer=l2_normalizer,
            bm25=BM25,
            reranker=RERANKER,
            id_to_text=ID_TO_TEXT,
            docs_ids_ordered=DOCS_IDS_ORDERED,
            docs_texts_ordered=DOCS_TEXTS_ORDERED,
            metadata_filter=metadata_filter
        )

        print("\n💬 Final Answer:\n")
        print(answer)
        print("\n" + "-" * 80)
            


        

