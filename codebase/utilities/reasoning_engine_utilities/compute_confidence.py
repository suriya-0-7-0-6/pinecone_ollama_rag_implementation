def compute_confidence_original(candidates, response):
    if not candidates:
        return 0.0

    scores = [score for _, score in candidates]
    avg_relevance = float(sum(scores) / len(scores))

    # Citation coverage: how many retrieved chunks were referenced?
    total_chunks = len(candidates)
    referenced = sum(1 for i in range(1, total_chunks+1) if f"[{i}]" in response)
    citation_ratio = referenced / total_chunks if total_chunks > 0 else 0.0

    confidence = (0.7 * avg_relevance) + (0.3 * citation_ratio)
    return round(confidence, 3)


def compute_confidence(top_score, num_chunks, citations):
    citation_factor = 1 if citations else 0.4
    retrieval_strength = min(1.0, top_score * (num_chunks / 5))  
    hallucination_penalty = 0.2 if not citations else 0

    return round(max(0.05, retrieval_strength * citation_factor - hallucination_penalty), 2)