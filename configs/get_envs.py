from dotenv import load_dotenv
from pathlib import Path
import sys
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_CONFIGS_FILE = PROJECT_ROOT / 'configs' / '.env'
sys.path.append(PROJECT_ROOT)
load_dotenv()

class CONFIG:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_INDEX = os.getenv('PINECONE_INDEX')
    PINECONE_REGION = os.getenv('PINECONE_REGION')
    EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME', 'all-MiniLM-L6-v2')
    DEFAULT_NAMESPACE = ""
    ITERACTIVE_CACHE = os.getenv('ITERACTIVE_CACHE', 'true').lower() in ('1', 'true', 'yes')
    N_CANDIDATES = int(os.getenv('N_CANDIDATES', '20'))
    TOP_K_TO_RETURN = int(os.getenv('TOP_K_TO_RETURN', '3'))
    SCORE_THRESHOLD = float(os.getenv('SCORE_THRESHOLD', '0.20'))
    RERANKER_MODEL = os.getenv('RERANKER_MODEL', 'cross-encoder/ms-marco-MiniLM-L-6-v2')
    CROSS_ENCODER_AVAILABLE = os.getenv('CROSS_ENCODER_AVAILABLE', True)
    BM25_AVAILABLE = os.getenv('BM25_AVAILABLE', 'true').lower() in ('1', 'true', 'yes')
    USE_HYBRID = os.getenv('USE_HYBRID', 'true').lower() in ('1', 'true', 'yes')
    CHUNK_SIZE_CHARS = int(os.getenv('CHUNK_SIZE_CHARS', 1000))
    CHUNK_OVERLAP_CHARS = int(os.getenv('CHUNK_OVERLAP_CHARS', 200))
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))
    RAG_OUTPUT_STYLE = os.getenv('RAG_OUTPUT_FORMAT', "auto")
    RAG_RUN_MODE = os.getenv('RAG_RUN_MODE', "api")
    RAG_DEBUG = os.getenv('RAG_DEBUG', 'true').lower() in ('1', 'true', 'yes')
    
    DOCS_DIR =  PROJECT_ROOT / Path(os.getenv('DOCS_DIR', 'uploads'))
    CODEBASE_DIR = PROJECT_ROOT / Path(os.getenv('CODEBASE_DIR', 'codebase'))
    CODE_UTILS_DIR = CODEBASE_DIR / Path(os.getenv('CODE_UTILS_DIR', 'code_utilities'))
    LOGS_DIR = PROJECT_ROOT / Path(os.getenv('LOGS_DIR', 'logs'))
    MAPPING_FILE = LOGS_DIR / Path(os.getenv('MAPPING_FILE', 'id_to_text_map.json'))
    CACHE_FILE = LOGS_DIR / Path(os.getenv('CACHE_FILE', 'query_cache.json'))
    NAMESPACE_FILE =  LOGS_DIR / Path(os.getenv('NAMESPACE_FILE', 'namespaces.json'))
    MONITORING_FILE = LOGS_DIR / Path(os.getenv('MONITORING_FILE', 'monitoring_logs.jsonl'))


    @staticmethod
    def ensure_directories():
        for folder in [
            CONFIG.DOCS_DIR,
            CONFIG.CODEBASE_DIR,
            CONFIG.CODE_UTILS_DIR,
            CONFIG.LOGS_DIR
        ]:
            folder.mkdir(parents=True, exist_ok=True)