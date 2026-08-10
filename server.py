"""Flask application for analyzing text and detecting emotions."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the provided text and return emotion scores and the dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"

    return (
        f"For the given statement, the system response is"
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}"
        f" and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

@app.route('/')
def index():
    """Render the application's home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
