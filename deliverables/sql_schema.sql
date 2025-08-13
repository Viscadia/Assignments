-- Products Table
CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL
);

-- Customers Table
CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_type VARCHAR(50),
    city VARCHAR(100),
    region VARCHAR(50),
    sales_rep VARCHAR(100)
);

-- Inventory Table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    stock_level Float NOT NULL,
    reorder_level INT,
    avg_daily_sales INT,
    days_until_reorder DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sales Table
CREATE TABLE sales (
    sale_id VARCHAR(20) PRIMARY KEY,
    sale_date DATE NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    quantity DECIMAL(12,2) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL,
    total_sale_amount DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);