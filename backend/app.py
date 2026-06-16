from sqlalchemy import create_engine, text
import os
from datetime import datetime, timezone
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_USER = "shopworlduser"
DB_PASSWORD = "ShopWorld123!"
DB_HOST = "35.205.42.214"
DB_NAME = "shopworld"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
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

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT id,name,category,price,image
            FROM products
        """))

        products = []

        for row in result:
            products.append({
                "id": row.id,
                "name": row.name,
                "category": row.category,
                "price": float(row.price),
                "image": row.image
            })

    return jsonify({
        "products": products,
        "source": "cloud-sql"
    })

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
