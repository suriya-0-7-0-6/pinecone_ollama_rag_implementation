import re

def extract_citations(response, retrieved_chunks):
    used_refs = sorted(set(map(int, re.findall(r"\[(\d+)\]", response))))

    citations = []
    for ref_num in used_refs:
        if ref_num-1 < len(retrieved_chunks):
            text, score, meta = retrieved_chunks[ref_num-1]
            citations.append({
                "reference": ref_num,
                "score": float(score),
                "metadata": meta,
                "snippet": text[:200] + "..." if len(text) > 200 else text
            })

    return citations