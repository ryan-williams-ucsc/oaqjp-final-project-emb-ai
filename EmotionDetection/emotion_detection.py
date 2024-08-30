import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myJSON = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myJSON, headers=header)
    formatted_response = json.loads(response.text)

    # formats dictionary to be returned
    if response.status_code == 200:
        emotions = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }
        # finds the max value and appends it to the return dictionary 
        dominant_emotion_name = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion_name
        return emotions
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions

    