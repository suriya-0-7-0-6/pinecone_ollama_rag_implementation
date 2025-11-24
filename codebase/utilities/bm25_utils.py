import numpy as np

def check_if_bm25_availability_and_build_index(app_config, doc_tokens_ordered):
    if app_config.BM25_AVAILABLE and app_config.USE_HYBRID and len(doc_tokens_ordered) > 0:
        from rank_bm25 import BM25Okapi
        bm25 = BM25Okapi(doc_tokens_ordered)
        print("✅ BM25 index built for hybrid retrieval.")
        return bm25
    else:
        print("BM25 not available. Skipping hybrid search!")
        return None


def get_bm25_score_for_cid(app_config, bm25, cid, query, docs_ids_ordered) -> float:
    if not (app_config.BM25_AVAILABLE and bm25):
        return 0.0
    try:
        idx = docs_ids_ordered.index(cid)
        tokens = query.lower().split()
        scores = bm25.get_scores(tokens)
        raw = float(scores[idx])
        return raw
    except ValueError:
        return 0.0
    

