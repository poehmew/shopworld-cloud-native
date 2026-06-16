CREATE TABLE products (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(120) NOT NULL,
  category VARCHAR(80) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  image_url VARCHAR(512)
);

CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_total DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO products (name, category, price, image_url) VALUES
('Cloud Hoodie', 'Apparel', 59.00, 'gs://shopworld-assets/hoodie.jpg'),
('Smart Backpack', 'Accessories', 89.00, 'gs://shopworld-assets/backpack.jpg'),
('Wireless Keyboard', 'Electronics', 49.00, 'gs://shopworld-assets/keyboard.jpg');
