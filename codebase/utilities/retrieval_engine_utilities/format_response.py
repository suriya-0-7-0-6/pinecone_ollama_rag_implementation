import os
import json

def format_response(app_config, response, citations, confidence, mode="hybrid", style="chat"):

    if style == "json":
        return json.dumps({
            "answer": response,
            "sources": citations,
            "retrieval_mode": mode,
            "confidence": confidence
        }, indent=2)
    
    elif style == "chat":
        formatted_sources = "\n".join([
            f"[{c['reference']}] {c['metadata'].get('file','unknown')} (score {c['score']:.3f})"
            for c in citations
        ])
        return f"""
📌 **Answer:**  
{response}

📚 **Sources Used:**  
{formatted_sources}

🧠 Mode: {mode.upper()}  
🔍 Confidence: {confidence:.2f}
        """.strip()

    run_mode = app_config.RAG_RUN_MODE
    return format_response(
        app_config,
        response,
        citations,
        confidence,
        mode,
        style="json" if run_mode == "api" else "chat"
    )