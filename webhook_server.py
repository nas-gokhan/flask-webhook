from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook route to handle incoming POST requests
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json  # Capture JSON payload from the incoming webhook
        print(f"Webhook received: {data}")  # Log the webhook data to the console
        return jsonify({"status": "success", "received": data}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

# Default route to avoid "Not Found" errors on the root URL
@app.route('/')
def index():
    return "Webhook Server is Running", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
