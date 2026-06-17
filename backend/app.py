from google.cloud import bigquery
from sqlalchemy import create_engine, text
import os
from datetime import datetime, timezone
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
bq_client = bigquery.Client()

DB_USER = os.environ.get("DB_USER", "shopworlduser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "ShopWorld123!")
DB_NAME = os.environ.get("DB_NAME", "shopworld")
INSTANCE_CONNECTION_NAME = os.environ.get(
    "INSTANCE_CONNECTION_NAME",
    "shopworld-demo:europe-west1:shopworld-mysql"
)

DB_HOST = f"/cloudsql/{INSTANCE_CONNECTION_NAME}"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}?unix_socket={DB_HOST}"
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

    rows = [{
        "id": int(datetime.now().timestamp()),
        "event_name": payload.get("event_name"),
        "product_name": payload.get("product_name"),
        "created_at": datetime.utcnow().isoformat()
    }]

    table_id = "shopworld-demo.shopworld_analytics.user_events"

    errors = bq_client.insert_rows_json(table_id, rows)

    if errors:
        return jsonify({"success": False, "errors": errors}), 500

    return jsonify({"success": True}), 201

@app.get("/")
def index():
    return jsonify({"message": "ShopWorld Backend API", "docs": ["/api/health", "/api/products"]})
@app.get("/api/orders")
def get_orders():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT id,
                   product_name,
                   price,
                   quantity,
                   created_at
            FROM orders
            ORDER BY created_at DESC
        """))

        orders = []

        for row in result:
            orders.append({
                "id": row.id,
                "product_name": row.product_name,
                "price": float(row.price),
                "quantity": row.quantity,
                "created_at": str(row.created_at)
            })

    return jsonify({"orders": orders})
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
