from flask import Flask, request, jsonify
import os
from waitress import serve

RECALL_API_KEY = os.getenv("RECALL_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok"})

@app.route("/agent", methods=["POST"])
def agent_handler():
    data = request.json
    user_input = data.get("input", "")

    # Jawaban agent (tulis logikamu sendiri)
    response_text = f"Halo! Kamu tadi bilang: {user_input}"

    # Format respons Recall
    return jsonify({
        "response": response_text
    })

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
