def load_reranker(Config):
    if Config.CROSS_ENCODER_AVAILABLE:
        try:
            from sentence_transformers import CrossEncoder
            RERANKER = CrossEncoder(Config.RERANKER_MODEL)
            print(f"Cross-encode loaded: {Config.RERANKER_MODEL}")
        except Exception as e:
            print(f"Failed to load cross-encode {Config.RERANKER_MODEL}: {e}")
            RERANKER = None
    return RERANKER