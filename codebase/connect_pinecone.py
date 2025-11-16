# from pinecone import Pinecone
# from pinecone.models import ServerlessSpec

# from sentence_transformers import SentenceTransformer

# pc = Pinecone(api_key="pcsk_5STqVY_Td5uE1AYPMY6fwLGhMcrHwZuBHo36vE8UBpRrQDe4M7wRap8x67RyECxAEWW73S")
# print("Connected to Pinecone successfully.")

# print(pc.list_indexes())

# index_name = "my-test-index"
# spec = ServerlessSpec(
#     cloud="aws",
#     region="us-east-1"
# )

# try:
#     if index_name not in pc.list_indexes():
#         pc.create_index(
#             name=index_name,
#             dimension=384,
#             metric="cosine",
#             spec=spec
#         )
#         print(f"Index '{index_name}' created.")
#     else:
#         print(f"Index '{index_name}' already exists.")
# except Exception as e:
#     if "ALREADY_EXISTS" in str(e):
#         print(f"⚠️ Index '{index_name}' already exists (handled gracefully).")
#     else:
#         raise e
# index = pc.Index(index_name)
# print(f"Using index: {index_name}")


# embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# texts = [
#     "I love learning about machine learning and AI.",
#     "Deep learning enables image and speech recognition.",
#     "Pinecone is a vector database used for similarity search.",
#     "Flask is a lightweight web framework for Python."
# ]

# embeddings = embedding_model.encode(texts).tolist()
# print(f"✅ Generated {len(embeddings)} embeddings, each with {len(embeddings[0])} dimensions.")


# to_upsert = [
#     (f"id-{i}", embeddings[i], {"text": texts[i]})
#     for i in range(len(texts))
# ]

# index.upsert(vectors=to_upsert)
# print(f"✅ Upserted {len(to_upsert)} vectors into the index '{index_name}'.")

# query_text = "Which technology is used for semantic search?"
# query_vector = embedding_model.encode([query_text]).tolist()

# results = index.query(
#     vector=query_vector,
#     top_k=2,
#     include_metadata=True
# )

# print(results)

# print(f"\nQuery Results for: '{query_text}'")
# for match in results['matches']:
#     print(f"Score: {match['score']:.4f} | Text: {match['metadata']['text']}")


from pinecone import Pinecone
from pinecone.models import ServerlessSpec
from sentence_transformers import SentenceTransformer

pc = Pinecone(api_key="pcsk_5STqVY_Td5uE1AYPMY6fwLGhMcrHwZuBHo36vE8UBpRrQDe4M7wRap8x67RyECxAEWW73S")
print("Connected to Pinecone successfully.")

existing_indexes = pc.list_indexes()
print("Existing indexes:", existing_indexes)

index_name = "my-text-index"

spec = ServerlessSpec(
    cloud="aws",
    region="us-east-1"
)

if index_name not in [idx["name"] for idx in existing_indexes]:
    pc.create_index(
        name=index_name,
        dimension=384,
        spec=spec,
        metric="cosine"
    )
    print(f"Indes '{index_name} created.")
else:
    print(f"Index '{index_name}' already exists.")

index = pc.Index(index_name)
print(f"Using index: {index_name}")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Loaded embedding model.")

texts = [
    "I love learning about machine learning and AI.",
    "Deep learning enables image and speech recognition.",
    "Pinecone is a vector database used for similarity search.",
    "Flask is a lightweight web framework for Python."
]

embeddings = embedding_model.encode(texts).tolist()
print(f"✅ Generated {len(embeddings)} embeddings.")
print(f"🔹 Each embedding dimension: {len(embeddings[0])}\n")

import numpy as np
print("📊 Example Embedding (first 5 dimensions):")
print(np.array(embeddings[0])[:5], "...\n")

print("✅ Pinecone connection and embedding generation complete!")


to_upsert = [
    (f"vec-{i}", embeddings[i], {"text": texts[i], "category": "AI"})
    for i in range(len(texts))
]

index.upsert(vectors=to_upsert)
print(f"✅ Upserted {len(to_upsert)} vectors into the index '{index_name}'.")  

fetch_result = index.fetch(ids=["vec-1"])
print("✅ Fetched vector 'vec-1':", fetch_result)

query_text = "Which company helps with semantic search databases?"
query_vector = embedding_model.encode([query_text]).tolist()

results = index.query(
    vector=query_vector,
    top_k=2,
    include_metadata=True
)

print(f"Query Results for: '{query_text}'")
for match in results['matches']:
    print(f"Score: {match['score']:.4f} | Text: {match['metadata']['text']}")

index.delete(ids=["vec-3"])
print("✅ Deleted vector 'vec-3' from the index.")