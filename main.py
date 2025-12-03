from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok"})

@app.route("/agent", methods=["POST"])
def agent_handler():
    data = request.json
    return jsonify({
        "response": f"Agent received: {data}"
    })

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
