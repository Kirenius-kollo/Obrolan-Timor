from flask import Flask, request, jsonify
import requests
from transformers import pipeline
import boto3

app = Flask(__name__)

# Initialize Bible API
def get_bible_verse(book, chapter, verse, translation='kjv'):
    url = f"https://bible-api.com/{book}%20{chapter}:{verse}?translation={translation}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Initialize Chatbot
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def chat_with_bot(user_input):
    response = chatbot(user_input)
    return response[0]['generated_text']

# Initialize AWS S3
s3_client = boto3.client('s3')

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def download_from_s3(bucket, object_name, file_name):
    response = s3_client.download_file(bucket, object_name, file_name)
    return response

@app.route('/bible', methods=['GET'])
def bible():
    book = request.args.get('book')
    chapter = request.args.get('chapter')
    verse = request.args.get('verse')
    translation = request.args.get('translation', 'kjv')
    verse_data = get_bible_verse(book, chapter, verse, translation)
    return jsonify(verse_data)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chat_with_bot(user_input)
    return jsonify({"response": response})

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    bucket = request.form['bucket']
    file.save(file.filename)
    upload_to_s3(file.filename, bucket)
    return jsonify({"message": "File uploaded successfully"})

@app.route('/download', methods=['GET'])
def download():
    bucket = request.args.get('bucket')
    object_name = request.args.get('object_name')
    file_name = request.args.get('file_name')
    download_from_s3(bucket, object_name, file_name)
    return jsonify({"message": "File downloaded successfully"})

if __name__ == '__main__':
    app.run(debug=True)
