# app/emotion.py
from typing import Dict
import json

def parse_emotion_response(nlu_response: Dict) -> Dict:
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotions = response["emotion"]["document"]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }

def pretty_json(output: Dict) -> str:
    return json.dumps(output, indent=2)
