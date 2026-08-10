from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():

    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    return (
        f"For the given statement, the system response is"
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}"
        f" and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is <strong>{emotions['dominant_emotion']}</strong>."
    )

@app.route('/')
def index():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)