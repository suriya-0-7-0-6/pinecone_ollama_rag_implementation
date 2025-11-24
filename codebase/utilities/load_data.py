
from pathlib import Path
import pdfplumber
import os
import json
from bs4 import BeautifulSoup

def load_txt(path: Path) -> str:
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        return f.read()
    
def load_pdf(path: Path) -> str:
    text_parts = []
    with pdfplumber.open(path) as pdf:
        i = 0
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return '\n'.join(text_parts)

def load_html(path: Path) -> str:
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    for s in soup(['script', 'style']):
        s.decompose()

    return soup.get_text(separator='\n')


def load_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == '.txt':
        return load_txt(path)
    elif suffix == '.pdf':
        return load_pdf(path)
    elif suffix in ['.html', '.htm']:
        return load_html(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
    

def get_data_from_mapping_file(Config):
    id_to_text = {}
    doc_ids_ordered = []
    doc_texts_ordered = []
    doc_tokens_ordered = []
    if os.path.exists(Config.MAPPING_FILE):
        with open(Config.MAPPING_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                    cid = item.get("id")
                    text = item.get("text")
                    if cid:
                        id_to_text[cid] = {"text": text, "metadata": item.get("metadata", {})}
                        doc_ids_ordered.append(cid)
                        doc_texts_ordered.append(text)
                        if Config.BM25_AVAILABLE:
                            tokens = text.lower().split()
                            doc_tokens_ordered.append(tokens)
                except Exception:
                    continue
        print(f"📂 Loaded mapping for {len(id_to_text)} chunks from {Config.MAPPING_FILE}")
        return id_to_text, doc_ids_ordered, doc_texts_ordered, doc_tokens_ordered
    else:
        print(f"⚠️ Mapping file '{Config.MAPPING_FILE}' not found. Retrieval will still use metadata if present in Pinecone.")
        return id_to_text, doc_ids_ordered, doc_texts_ordered, doc_tokens_ordered

    
