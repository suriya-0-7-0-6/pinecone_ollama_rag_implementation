from typing import List, Tuple

def chunk_text_by_chars(text: str, chunk_size: int, overlap: int) -> List[Tuple[int, int, str]]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")
    step = chunk_size - overlap
    if step <= 0:
        raise ValueError("Overlap must be smaller than chunk size.")
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append((start, end, chunk))
            start += step
    return chunks


# def chunk_text_smart(text: str, chunk_size: int, overlap: int) -> List[Tuple[int, int, str]]:
#     paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
#     chunks = []
#     current = ""
#     char_idx = 0
#     pointer = 0

#     print(f"Paragraphs: {paragraphs}")
#     for p in paragraphs:
#         if len(current) + len(p) + 2 <= chunk_size:
#             current = (current + "\n\n" + p).strip() if current else p
#         else:
#             if current:
#                 start = text.find(current, pointer)
#                 end = start + len(current)
