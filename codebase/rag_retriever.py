import os
import json
import requests
from typing import List
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')
PINECONE_REGION = os.getenv('PINECONE_REGION')
EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME')
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

print(f"\n🔧 Loaded environment:")
print(f"  Pinecone Index: {PINECONE_INDEX}")
print(f"  Ollama URL: {OLLAMA_URL}")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)
model = SentenceTransformer(EMBEDDING_MODEL_NAME)
mapping_file_path = "id_to_text_map.json"
id_to_text = {}

with open(mapping_file_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            item = json.loads(line)
            id_to_text[item["id"]] = item


def generate_query_embedding(query_text: str) -> List[float]:
    print(f"\n🧠 Generating embedding for query: '{query_text}'")
    embedding = model.encode([query_text])[0].tolist()
    print(f"✅ Embedding dimension: {len(embedding)}")
    return embedding


def retrieve_relevant_chunks(query_embedding: List[float], top_k: int = 5):
    print(f"\n🔍 Querying Pinecone for top {top_k} matches...")
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        namespace="my_corpus"
    )
    matches = results["matches"]
    print(f"✅ Retrieved {len(matches)} matches.")
    context_chunks = []
    for match in matches:
        chunk_text = match["metadata"].get("text") or id_to_text.get(match["id"], "")
        score = match["score"]
        context_chunks.append((chunk_text, score))
        print(f"   - ID: {match['id']}  (Score: {score:.4f})")
    return context_chunks

def build_prompt(query_text, retrieved_chunks):
    context_text = "\n\n".join(retrieved_chunks)
    prompt = f"""
You are an AI assistant with access to the following contextual information:

{context_text}

Based on the above context, answer the following user query accurately and concisely.
If the answer is not in the context, say "I couldn't find relevant information."

User Query: {query_text}
"""
    print("\n🧩 Prompt constructed successfully.")
    return prompt.strip()


query_embedding = generate_query_embedding("What are the five Blue Zones?")
context_chunks = retrieve_relevant_chunks(query_embedding, top_k=5)

print("\n📄 Retrieved Context Chunks:")
for i, (chunk, score) in enumerate(context_chunks):
    print(f"\n--- Chunk {i+1} (Score: {score:.4f}) ---\n{chunk}\n")