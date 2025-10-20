# app/emotion.py
from typing import Dict
import json

def parse_emotion_response(nlu_response: Dict) -> Dict:
    """
    Extract and normalize Watson emotion scores into a simple dict:
    { 'joy': 0.12, 'sadness': 0.03, ... }
    """
    try:
        emotion = nlu_response.get("emotion", {})
        document = emotion.get("document", {})
        scores = document.get("emotion", {})
        # ensure keys present and floats
        return {k: float(scores.get(k, 0.0)) for k in ["joy","sadness","fear","disgust","anger"]}
    except Exception:
        return {"joy":0,"sadness":0,"fear":0,"disgust":0,"anger":0}

def pretty_json(output: Dict) -> str:
    return json.dumps(output, indent=2)
