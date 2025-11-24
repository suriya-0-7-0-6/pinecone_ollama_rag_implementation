def build_prompt(query_text, retrieved_candidates):
    pieces = []
    for i, (chunk, score, metadata) in enumerate(retrieved_candidates):
        pieces.append(f"[{i+1}] (score: {score:.3f})\n{chunk}")
    context_text = "\n\n".join(pieces)
    SYSTEM_INSTRUCTIONS = """You are a Retrieval-Augmented Assistant.
Rules:
1. Use ONLY the provided context.
2. Always cite context numbers: [1], [2], etc.
3. If unsure or context missing, respond: "No relevant context found.".
4. Do NOT guess or hallucinate.
"""
    prompt = f"{SYSTEM_INSTRUCTIONS}\n\nCONTEXT:\n{context_text}\n\nUSER QUESTION:\n{query_text}\n\nASSISTANT RESPONSE:"
    return prompt.strip()