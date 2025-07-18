from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import certifi
from googleapiclient import discovery
import json
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# SSL証明書の設定
os.environ['SSL_CERT_FILE'] = certifi.where()

load_dotenv()

API_KEY = os.getenv('PERSPECTIVE_API_KEY')

def analyze_toxicity(text):
    """Perspective APIを使用してテキストの毒性を分析"""
    try:
        client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=API_KEY,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
        )

        analyze_request = {
            'comment': {'text': text},
            'requestedAttributes': {
                'TOXICITY': {},
                'SEVERE_TOXICITY': {},
                'IDENTITY_ATTACK': {},
                'INSULT': {},
                'PROFANITY': {},
                'THREAT': {}
            }
        }

        response = client.comments().analyze(body=analyze_request).execute()
        return response
    except Exception as e:
        return {'error': str(e)}

@app.route('/')
def index():
    """メインページを表示"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """テキスト分析エンドポイント"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'テキストが入力されていません'}), 400
        
        result = analyze_toxicity(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': f'エラーが発生しました: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)