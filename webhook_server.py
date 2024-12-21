from flask import Flask, request, jsonify
from alpaca_trade_api.rest import REST

# Alpaca API keys (replace with your actual keys)
ALPACA_API_KEY = "PK1D4RGQRTXZI9K1YBRZ"
ALPACA_API_SECRET = "PK1D4RGQRTXZI9K1YBRZ"
BASE_URL = "https://paper-api.alpaca.markets/v2"  # Use live URL for real trading

# Alpaca client
alpaca = REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=BASE_URL)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)

    if "symbol" in data and "action" in data and "quantity" in data:
        symbol = data["symbol"]
        action = data["action"]
        quantity = data["quantity"]

        try:
            # Execute order
            alpaca.submit_order(
                symbol=symbol,
                qty=quantity,
                side=action,
                type="market",
                time_in_force="gtc"
            )
            return jsonify({"message": f"{action} {quantity}x {symbol} placed."}), 200
        except Exception as e:
            print("Error placing order:", e)
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Invalid data format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))

