from flask import Flask, request, render_template, jsonify
import boto3
import io

app = Flask(__name__)

BUCKET = "face-recognition-free-test"
COLLECTION = "free-face-collection"
REGION = "ap-south-1"

s3 = boto3.client('s3', region_name=REGION)
rekognition = boto3.client('rekognition', region_name=REGION)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        file = request.files['image']
        filename = file.filename
        img_bytes = file.read()
        img_buffer = io.BytesIO(img_bytes)
        s3.upload_fileobj(img_buffer, BUCKET, f"uploads/{filename}")
        response = rekognition.search_faces_by_image(
            CollectionId=COLLECTION,
            Image={'Bytes': img_bytes},
            MaxFaces=5,
            FaceMatchThreshold=70
        )
        matches = []
        for match in response.get('FaceMatches', []):
            matches.append({
                'face_id': match['Face']['FaceId'],
                'confidence': round(match['Similarity'], 1),
                'external_id': match['Face'].get('ExternalImageId', 'Unknown')
            })
        return jsonify({'success': True, 'matches': matches})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
