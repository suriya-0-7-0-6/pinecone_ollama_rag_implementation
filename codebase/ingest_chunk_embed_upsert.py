import os
import json
import sys
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

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from configs.get_envs import CONFIG
CONFIG.ensure_directories()

def l2_normalize(vec):
    vec = np.array(vec)
    return (vec / (np.linalg.norm(vec) + 1e-10)).tolist()


def embed_and_upsert_docs(
        files: Iterable[Path],
        model: SentenceTransformer,
        pc_index,
        namespace: str = "default",
        chunk_size: int = CONFIG.CHUNK_SIZE_CHARS,
        overlap: int = CONFIG.CHUNK_OVERLAP_CHARS,
        batch_size: int = CONFIG.BATCH_SIZE,
        save_mapping_path: str = CONFIG.MAPPING_FILE,
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
                "tokens": chunk_text.lower().split(),
                "text": chunk_text
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
    print(f"Loading embedding mode: {CONFIG.EMBEDDING_MODEL_NAME}...")
    model = SentenceTransformer(CONFIG.EMBEDDING_MODEL_NAME)
    print("Model loaded.")

    pc = Pinecone(api_key=CONFIG.PINECONE_API_KEY)

    print("Listing existing Pinecone indexes...")
    existing = [i["name"] for i in pc.list_indexes()]    
    print(f"Existing indexes: {existing}")
    if CONFIG.PINECONE_INDEX not in existing:
        pc.create_index(
            name=CONFIG.PINECONE_INDEX,
            dimension=model.get_sentence_embedding_dimension(),
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=CONFIG.PINECONE_REGION)
        )
    else:
        print(f"Index {CONFIG.PINECONE_INDEX} already exists. Reusing it.")

    index = pc.Index(CONFIG.PINECONE_INDEX)

    

    doc_dir = Path(CONFIG.DOCS_DIR)
    all_files = [file for file in doc_dir.rglob("*") if file.suffix.lower() in [".txt", ".pdf", ".html", ".htm"]]
    
    print(f"Found {len(all_files)} files to process.")
    print(all_files)

    embed_and_upsert_docs(
        files=all_files,
        model=model,
        pc_index=index,
        namespace=CONFIG.DEFAULT_NAMESPACE,
        chunk_size=CONFIG.CHUNK_SIZE_CHARS,
        overlap=CONFIG.CHUNK_OVERLAP_CHARS,
        batch_size=CONFIG.BATCH_SIZE,
        save_mapping_path=CONFIG.MAPPING_FILE
    )

if __name__ == "__main__":  
    main()