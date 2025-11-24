import time
import json

def log_event(event, app_config):
    event['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(app_config.MONITORING_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")