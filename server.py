"""
handles all the routing from website
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    handles all requests to the API
    """
    text_to_analyse = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    emotions = emotion_detector(text_to_analyse)

    # Extract the dominant emotion
    dominant_emotion = emotions.pop('dominant_emotion')

    if dominant_emotion is None:
        return 'Invalid text, please try again'

    # Format the response string
    formatted_response_str = ', '.join([f"'{key}': {value}" for key, value in emotions.items()])
    return f"""For the given statement, the system response is {formatted_response_str}.
        \nThe dominant emotion is {dominant_emotion}."""

@app.route('/')
def render():
    """
    renders html page on load
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
