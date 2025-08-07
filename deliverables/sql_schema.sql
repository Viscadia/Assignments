-- Schema for customers table
CREATE TABLE customers (
    city VARCHAR(100),
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(255),
    region VARCHAR(50),
    sales_rep VARCHAR(50),
    type VARCHAR(50)
);

-- Schema for Products table
CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Schema for Inventory table
CREATE TABLE inventory (
    warehouse_id VARCHAR(20),
    product_id VARCHAR(20),
    stock_level INT,
    reorder_level INT,
    avg_daily_sales FLOAT,
    days_until_reorder FLOAT,
    PRIMARY KEY (warehouse_id, product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Schema for Sales table
CREATE TABLE sales (
    sale_id VARCHAR(20) PRIMARY KEY,
    sale_date DATE,
    product_id VARCHAR(20),
    customer_id VARCHAR(20),
    quantity INT,
    product_price DECIMAL(10, 2),
    total_sale_amount DECIMAL(12, 2),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
