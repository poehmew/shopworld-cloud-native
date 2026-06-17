import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { ShoppingBag, ShieldCheck, Zap, Database } from "lucide-react";
import "./style.css";

const API_BASE =
  import.meta.env.VITE_API_BASE_URL ||
  "https://shopworld-backend-37435775554.europe-west1.run.app";

const fallback = [
  { id: 1, name: "Cloud Hoodie", price: 59, category: "Apparel" },
  { id: 2, name: "Smart Backpack", price: 89, category: "Accessories" },
  { id: 3, name: "Wireless Keyboard", price: 49, category: "Electronics" },
];

function App() {
  const [products, setProducts] = useState(fallback);
  const [status, setStatus] = useState("demo fallback");
  const [cart, setCart] = useState([]);
  const [orders, setOrders] = useState([]);

  useEffect(() => {
  fetch(`${API_BASE}/api/products`)
    .then((r) => r.json())
    .then((data) => {
      setProducts(data.products || fallback);
      setStatus("connected to Cloud Run backend API");
    })
    .catch(() => setStatus("frontend running; backend API not configured"));

  fetch(`${API_BASE}/api/orders`)
    .then((r) => r.json())
    .then((data) => setOrders(data.orders || []));
}, []);
  const removeFromCart = (indexToRemove) => {
    setCart(
      cart.filter((_, index) => index !== indexToRemove)
    );
  };
  const addToCart = async (product) => {
    await fetch(`${API_BASE}/api/orders`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        product_id: product.id,
        product_name: product.name,
        price: product.price,
        quantity: 1,
      }),
    });

    console.log(`${product.name} added to cart`);
    setCart((currentCart) => [...currentCart, product]);
  };

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">ShopWorld modernization PoC</p>
          <h1>Cloud-native e-commerce demo on Google Cloud Run</h1>
          <p className="sub">
            Frontend + Backend API microservices prepared for Cloud SQL, Cloud Storage and BigQuery integration.
          </p>
          <div className="badges">
            <span>{status}</span>
            <span>serverless</span>
            <span>auto scaling</span>
          </div>
        </div>
        <ShoppingBag size={96} />
      </section>

      <section className="metrics">
        <div><Zap/><b>Scalable</b><p>Cloud Run handles traffic spikes.</p></div>
        <div><ShieldCheck/><b>Secure</b><p>IAM, IAP, Cloud Armor, Secret Manager.</p></div>
        <div><Database/><b>Data-driven</b><p>Cloud SQL + BigQuery analytics.</p></div>
      </section>
     <section className="cart-summary">
       <h2>Shopping Cart</h2>

       {cart.length === 0 ? (
         <p>No items in cart yet.</p>
        ) : (
          <div className="cart-list">
            {cart.map((item, index) => (
              <div className="cart-row" key={index}>
                <span>{item.name}</span>

                <div>
                  <strong>${item.price}</strong>

                  <button
                    className="remove-btn"
                    onClick={() => removeFromCart(index)}
                  >
                    Remove
                  </button>
                </div>
              </div>
              ))}
            </div>
          )}
          <p>Items: {cart.length}</p>
          <p>
          Total: $
          {cart.reduce((total, item) => total + Number(item.price), 0)}
        </p>
      </section>
      <section className="cart-summary">
        <h2>Order History</h2>

        {orders.slice(0, 10).map((o) => (
          <div className="cart-row" key={o.id}>
            <span>{o.product_name}</span>
            <strong>${o.price}</strong>
          </div>
        ))}
      </section>
      <section className="products">
        {products.map((p) => (
          <article key={p.id}>
            {p.image && <img src={p.image} alt={p.name} className="product-img" />}
            <h3>{p.name}</h3>
            <p>{p.category}</p>
            <strong>${p.price}</strong>
            <button className="cart-btn" onClick={() => addToCart(p)}>
              Add to Cart
            </button>
          </article>
        ))}
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
