from flask import Flask, jsonify
from routes.emails import emails_bp
from routes.orders import orders_bp
import os

app = Flask(__name__)

app.register_blueprint(emails_bp)
app.register_blueprint(orders_bp)

@app.route('/api/')
def home():
    return jsonify({
        "message": "Welcome to the Electronics Store API",
        "endpoints": {
            "api/emails": "GET - Fetch all emails",
            "api/orders": "GET - Fetch all orders"
        }
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
