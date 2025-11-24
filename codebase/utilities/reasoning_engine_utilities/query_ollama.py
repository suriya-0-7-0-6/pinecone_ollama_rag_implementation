import requests
import json

def query_ollama(app_config, prompt, model_name="gpt-oss:20b"):
    print(f"\n⚡ Sending prompt to Ollama ({model_name}) — length {len(prompt)} chars")
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    response = requests.post(app_config.OLLAMA_URL, json=payload)
    response.raise_for_status()
    response_json = response.json()
    if "message" in response_json and "content" in response_json["message"]:
        return response_json["message"]["content"]
    if "response" in response_json:
        return response_json["response"]
    print("✅ Received response from Ollama.")
    return json.dumps(response_json)