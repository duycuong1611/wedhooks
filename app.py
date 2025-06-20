# Python Flask 예시 (app.py)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        print("Received webhook data:", data)
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        print("Received non-JSON data:", request.data)
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True) # 예시 포트 5000
# This is a test change for webhook