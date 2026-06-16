import os
from datetime import datetime, timezone
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PRODUCTS = [
    {"id": 1, "name": "Cloud Hoodie", "price": 59.0, "category": "Apparel", "image": "https://storage.googleapis.com/shopworld-demo-assets/hoodie.jpg"},
    {"id": 2, "name": "Smart Backpack", "price": 89.0, "category": "Accessories", "image": "https://storage.googleapis.com/shopworld-demo-assets/backpack.jpg"},
    {"id": 3, "name": "Wireless Keyboard", "price": 49.0, "category": "Electronics", "image": "https://storage.googleapis.com/shopworld-demo-assets/keyboard.jpg"},
]

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "shopworld-backend",
        "runtime": "Cloud Run ready",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })

@app.get("/api/products")
def products():
    # In production this endpoint would read from Cloud SQL.
    return jsonify({"products": PRODUCTS, "source": "demo-api"})

@app.post("/api/events")
def events():
    payload = request.get_json(silent=True) or {}
    # In production this event could be exported to BigQuery for analytics.
    app.logger.info("shopworld_event=%s", payload)
    return jsonify({"accepted": True, "message": "Event logged for analytics"}), 202

@app.get("/")
def index():
    return jsonify({"message": "ShopWorld Backend API", "docs": ["/api/health", "/api/products"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
