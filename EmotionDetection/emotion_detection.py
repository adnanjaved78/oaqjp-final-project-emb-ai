import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json= payload, headers= headers, timeout=5)

    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None,
            'fear': None, 'joy': None, 
            'sadness': None, 'dominant_emotion': None}

    response_dictionary = json.loads(response.text)
    emotions_dictionary = response_dictionary["emotionPredictions"][0]["emotion"]

    emotions_dictionary["dominant_emotion"] = get_dominant_emotion(emotions_dictionary)

    return emotions_dictionary

def get_dominant_emotion(emotions):
    dominant = None
    highest = -1.0
    for emotion, score in emotions.items():
        if score > highest:
            highest = score
            dominant = emotion
    return dominant