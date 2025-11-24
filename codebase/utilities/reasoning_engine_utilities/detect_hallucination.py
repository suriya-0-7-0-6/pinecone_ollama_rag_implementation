def detect_hallucination(raw_response, candidates):
    num_refs = len(candidates)
    has_reference = any(f"[{i}]" in raw_response for i in range(1, num_refs+1))
    print(f"has_reference: {has_reference}")
    if not has_reference:
        return raw_response + "\n\n⚠️ *No matching context found — confidence low.*"
    print(f"Raw response has reference from retrieved context")
    return raw_response