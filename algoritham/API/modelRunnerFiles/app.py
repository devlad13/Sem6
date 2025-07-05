
from flask import Flask, request, jsonify
from model import predict_action

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    print("Received request")
    if 'video' not in request.files:
        return jsonify({'error': 'No video file found'}), 400
    
    video_file = request.files['video']
    clip_frames = [cv2.imdecode(np.fromstring(video_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)]
    
    action_label, confidence = predict_action(clip_frames)
    
    print("Prediction:", action_label, confidence)
    
    return jsonify({'action_label': action_label, 'confidence': confidence}), 200

if __name__ == '__main__':
    app.run(debug=True)
