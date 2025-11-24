import os
import sys
import json
import hashlib

def load_query_cache(Config):
    try:
        if os.path.exists(Config.CACHE_FILE):
            with open(Config.CACHE_FILE, 'r', encoding='utf-8') as f:
                QUERY_CACHE = json.load(f)
        else:
            QUERY_CACHE = {}
        return QUERY_CACHE
    except Exception:
        QUERY_CACHE = {}
        return QUERY_CACHE
    

def save_query_cache(Config, QUERY_CACHE):
    with open(Config.CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(QUERY_CACHE, f, ensure_ascii=False, indent=2)


def generate_256_hash_for_query(query, metadata_filter, namespace):
    key_obj = {"q": query, "filter": metadata_filter, "namespace": namespace}
    key_str = json.dumps(key_obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(key_str.encode()).hexdigest()