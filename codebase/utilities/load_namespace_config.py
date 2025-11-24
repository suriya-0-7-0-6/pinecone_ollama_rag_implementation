import os
import json

def load_namespace_config(Config):
    namespace_configs = {}
    if os.path.exists(Config.NAMESPACE_FILE):
        with open(Config.NAMESPACE_FILE, 'r') as f:
            namespace_configs = json.load(f)
    else:
        namespace_configs = {
            'default_namespace': Config.DEFAULT_NAMESPACE,
            'active_namespace': Config.DEFAULT_NAMESPACE,
            'allowed_namespaces': [Config.DEFAULT_NAMESPACE]
        }
    return namespace_configs


def set_namespace(namespace, Config, NAMESPACE_CONFIG):
    if namespace not in NAMESPACE_CONFIG['allowed_namespaces']:
        print(f"No such namespace present in {Config.PINECONE_INDEX} index.")
        print(f"Using default namespace.")
        NAMESPACE_CONFIG['active_namespace'] = Config.DEFAULT_NAMESPACE
    else:
        NAMESPACE_CONFIG['active_namespace'] = namespace
        print(f"🌐 Active namespace set to: {namespace}")
    with open(Config.NAMESPACE_FILE, 'w') as f:
        json.dump(NAMESPACE_CONFIG, f, indent=2)
    

def get_active_namespace(Config, NAMESPACE_CONFIG):
    return NAMESPACE_CONFIG.get("active_namespace", Config.DEFAULT_NAMESPACE)