def generate_query_embedding(query_text, embedding_model, l2_normalizer):
    print(f"\n🧠 Generating embedding for query: '{query_text}'")
    query_embedding = embedding_model.encode([query_text])[0]
    query_embedding = l2_normalizer(query_embedding)
    print(f"✅ Embedding dimension: {len(query_embedding)}")
    return query_embedding