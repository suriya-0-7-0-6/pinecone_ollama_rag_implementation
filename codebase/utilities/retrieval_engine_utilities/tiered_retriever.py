from utilities.retrieval_engine_utilities.retrieved_candidates import retrieve_candidates
import numpy as np

def tiered_retriever(
        app_config,
        query_embedding,
        query_text,
        pinecone_index,
        namespace,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        docs_texts_ordered,
        metadata_filter=None
    ):
    # TIER 1
    candidates = retrieve_candidates(
        app_config,
        query_embedding,
        query_text,
        pinecone_index,
        namespace,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        metadata_filter=metadata_filter,
        min_score=app_config.SCORE_THRESHOLD,
    )
    if candidates:
        return candidates, "hybrid"
    
    # TIER 2
    candidates = retrieve_candidates(
        app_config,
        query_embedding,
        query_text,
        pinecone_index,
        namespace,
        bm25,
        reranker,
        id_to_text,
        docs_ids_ordered,
        metadata_filter=metadata_filter,
        min_score=app_config.SCORE_THRESHOLD
    )
    if candidates:
        return candidates, "vector"
    
    # TIER 3 - BM25 only
    if bm25:
        tokens = query_text.lower().split()
        scores = bm25.get_scores(tokens)
        best_idx = int(np.argmax(scores))
        return [(docs_texts_ordered[best_idx], float(scores[best_idx]))], "bm25"
    
    return [], "none"