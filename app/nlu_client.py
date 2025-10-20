# app/nlu_client.py
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

class WatsonNLUClient:
    def __init__(self, apikey=None, url=None, version='2021-08-01'):
        apikey = apikey or os.getenv("WATSON_APIKEY")
        url = url or os.getenv("WATSON_URL")
        if not apikey or not url:
            raise ValueError("WATSON_APIKEY and WATSON_URL must be set")
        self.authenticator = IAMAuthenticator(apikey)
        self.client = NaturalLanguageUnderstandingV1(
            version=version,
            authenticator=self.authenticator
        )
        self.client.set_service_url(url)

    def analyze_emotion(self, text: str):
        response = self.client.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        return response
