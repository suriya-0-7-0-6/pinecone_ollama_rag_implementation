import os
import json
from pathlib import Path
from typing import List, Dict, Tuple, Iterable
from tqdm import tqdm
from dotenv import load_dotenv

import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from pinecone.models import ServerlessSpec

from utilities.load_data import load_file
from utilities.chunk_data import chunk_text_by_chars
from utilities.get_structure import explore_structure

import pdfplumber
from bs4 import BeautifulSoup

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')
PINECONE_REGION = os.getenv('PINECONE_REGION')
EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME')
DOCS_DIR = "../uploads"
NAMESPACE = "my_corpus"
CHUNK_SIZE_CHARS = int(os.getenv('CHUNK_SIZE_CHARS'))
CHUNK_OVERLAP_CHARS = int(os.getenv('CHUNK_OVERLAP_CHARS'))
BATCH_SIZE = int(os.getenv('BATCH_SIZE'))
SAVE_MAPPING_PATH = os.getenv('SAVE_MAPPING_PATH')

print(PINECONE_API_KEY, PINECONE_INDEX, PINECONE_REGION, EMBEDDING_MODEL_NAME, CHUNK_SIZE_CHARS, CHUNK_OVERLAP_CHARS, BATCH_SIZE, SAVE_MAPPING_PATH)

def l2_normalize(vec):
    """Return vector normalized to unit length"""
    vec = np.array(vec)
    return (vec / (np.linalg.norm(vec) + 1e-10)).tolist()


def embed_and_upsert_docs(
        files: Iterable[Path],
        model: SentenceTransformer,
        pc_index,
        namespace: str = "default",
        chunk_size: int = CHUNK_SIZE_CHARS,
        overlap: int = CHUNK_OVERLAP_CHARS,
        batch_size: int = BATCH_SIZE,
        save_mapping_path: str = SAVE_MAPPING_PATH,
):
    id_to_text = {}
    vectors_buffer = []
    meta_buffer = []
    ids_buffer = []


    for file_path in files:
        fname = file_path.name
        print(f"Processing file: {fname}")
        try:
            text = load_file(file_path)
        except Exception as e:
            print(f"Failed to load {fname}: {e}")
            continue

        text = text.replace("\r\n", "\n").strip()
        if not text:
            print("Empty content, skipping.")
            continue

        chunks = chunk_text_by_chars(text, chunk_size, overlap)
        print(f"  - {len(chunks)} chunks created.")

        for idx, (start, end, chunk_text) in enumerate(chunks):
            # Build unique ID: safe characters only
            safe_fname = fname.replace(" ", "_")
            cid = f"{safe_fname}__chunk_{idx}"

            metadata = {
                "source": fname,
                "chunk_index": idx,
                "start_char": int(start),
                "end_char": int(end),
                "namespace": namespace,
                "tokens": chunk_text.lower().split()
            }

            id_to_text[cid] = {
                "id": cid,
                "text": chunk_text,
                "metadata": metadata
            }

            ids_buffer.append(cid)
            meta_buffer.append(metadata)
            vectors_buffer.append(chunk_text)

            if len(vectors_buffer) >= batch_size:
                embed_and_upsert_batch(
                    vectors_buffer, ids_buffer, meta_buffer, model, pc_index, namespace
                )
                with open(save_mapping_path, "a", encoding="utf-8") as f:
                    for entry in id_to_text.values():
                        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                id_to_text = {}
                ids_buffer, meta_buffer, vectors_buffer = [], [], []

    if vectors_buffer:
        embed_and_upsert_batch(
            vectors_buffer, ids_buffer, meta_buffer, model, pc_index, namespace
        )
        with open(save_mapping_path, "a", encoding="utf-8") as f:
            for entry in id_to_text.values():
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        id_to_text = {}
        ids_buffer, meta_buffer, vectors_buffer = [], [], []


def embed_and_upsert_batch(texts: List[str], ids: List[str], metadata_list: List[Dict], model: SentenceTransformer, pc_index, namespace: str):
    print(f"Embedding and upserting batch of {len(texts)} vectors...")
    embeddings = model.encode(texts, show_progress_bar=False, batch_size=32)
    embeddings = [e.tolist() if hasattr(e, "tolist") else list(e) for e in embeddings]
    embeddings = [l2_normalize(e) for e in embeddings]
    upsert_tuples = []
    for cid, embedding, metadata in zip(ids, embeddings, metadata_list):
        upsert_tuples.append((cid, embedding, metadata))

    try:
        pc_index.upsert(vectors=upsert_tuples, namespace=namespace)
    except Exception as e:
        print(f"Upsert error (attempting retry): {e}")
        mini_batch_size = 16
        for i in range(0, len(upsert_tuples), mini_batch_size):
            try:
                batch = upsert_tuples[i:i + mini_batch_size]
                pc_index.upsert(vectors=batch, namespace=namespace)
            except Exception as e:
                print(f"  - Failed to upsert batch starting at index {i}: {e}")
    print(f"📤 Upserted batch of {len(upsert_tuples)} vectors to namespace='{namespace}'")


def main():
    pc = Pinecone(api_key=PINECONE_API_KEY)

    print("Listing existing Pinecone indexes...")
    existing = [i["name"] for i in pc.list_indexes()]    
    print(f"Existing indexes: {existing}")
    if PINECONE_INDEX not in existing:
        pc.create_index(
            name=PINECONE_INDEX,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_REGION)
        )
    else:
        print(f"Index {PINECONE_INDEX} already exists. Reusing it.")

    index = pc.Index(PINECONE_INDEX)

    print(f"Loading embedding mode: {EMBEDDING_MODEL_NAME}...")
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    print("Model loaded.")

    doc_dir = Path(DOCS_DIR)
    all_files = [file for file in doc_dir.rglob("*") if file.suffix.lower() in [".txt", ".pdf", ".html", ".htm"]]
    
    print(f"Found {len(all_files)} files to process.")
    print(all_files)

    embed_and_upsert_docs(
        files=all_files,
        model=model,
        pc_index=index,
        namespace=NAMESPACE,
        chunk_size=CHUNK_SIZE_CHARS,
        overlap=CHUNK_OVERLAP_CHARS,
        batch_size=BATCH_SIZE,
        save_mapping_path=SAVE_MAPPING_PATH
    )

if __name__ == "__main__":  
    main()