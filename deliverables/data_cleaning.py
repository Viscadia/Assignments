import pandas as pd
import glob
import os
import numpy as np

# File paths
PRODUCTS_PATH = "C:/Users/Lalit Prajapat/Downloads/a_data/a_data/products.xlsx"
CUSTOMERS_PATH = 'C:/Users/Lalit Prajapat/Downloads/a_data/a_data/customers.json'
INVENTORY_PATH = 'C:/Users/Lalit Prajapat/Downloads/a_data/a_data/inventory.xlsx'
SALES_GLOB = 'C:/Users/Lalit Prajapat/Downloads/a_data/a_data/sales/sales_day_*.csv'

# Loading data
def load_data():
    products = pd.read_excel(PRODUCTS_PATH)
    customers = pd.read_json(CUSTOMERS_PATH)
    inventory = pd.read_excel(INVENTORY_PATH)
    sales_files = glob.glob(SALES_GLOB)
    sales = pd.concat([pd.read_csv(f) for f in sales_files], ignore_index=True)
    return products, customers, inventory, sales

# EDA function to get overview of data 
def eda_report(df, name):
    print(f"--- {name} ---")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data types:\n", df.dtypes)
    print("Missing values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())
    print("Summary stats:\n", df.describe(include='all'))
    print("\n")

# Data cleaning functions

def clean_products(products):
    # to Remove white spaces 
    products = products.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    # to Remove duplicates and NaN values
    products = products.drop_duplicates()
    # to Ensure numeric for price
    products['price'] = pd.to_numeric(products['price'], errors='coerce')
    products = products.dropna(subset=['product_id', 'product_name', 'category', 'price'])
    # to Ensure Pattern for product_id 
    valid_pattern = r'^PID\d+$'
    products = products[products['product_id'].astype(str).str.match(valid_pattern)]
    return products

def clean_customers(customers):
    customers = customers.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    customers = customers.drop_duplicates()
    customers = customers.dropna(subset=['customer_id', 'customer_name', 'type', 'city', 'region', 'sales_rep'])
    # mapping some regions to correct spellings
    region_mapping = {
        'Swest': 'Southwest',
        'N/E': 'Northeast',
        'Suth': 'South',
        'Eest': 'East'
    }
    # Ensuring Pattern for customer_id
    valid_pattern = r'^C\d+$'
    customers = customers[customers['customer_id'].astype(str).str.match(valid_pattern)]
    customers['region'] = customers['region'].str.strip().str.title()
    customers['region'] = customers['region'].replace(region_mapping)
    return customers

def clean_inventory(inventory):
    # Force all object columns to be stripped of spaces/commas before comparing for duplicates
    for col in inventory.select_dtypes(include=['object']).columns:
        inventory[col] = inventory[col].astype(str).str.strip().str.replace(',', '')

    inventory = inventory.drop_duplicates()

    # Convert numeric columns properly
    numeric_cols = ['stock_level', 'reorder_level', 'avg_daily_sales']
    for col in numeric_cols:
        inventory[col] = pd.to_numeric(inventory[col], errors='coerce')

    # Drop rows where numeric columns are NaN
    inventory = inventory.dropna(subset=numeric_cols)

    # Validate patterns
    product_pattern = r'^PID\d+$'
    inventory = inventory[inventory['product_id'].str.match(product_pattern)]

    # Remove negative values
    inventory = inventory[(inventory['stock_level'] >= 0) & (inventory['reorder_level'] >= 0)]

    # Calculate days_until_reorder if avg_daily_sales != 0
    mask = (inventory['avg_daily_sales'] != 0) & (~inventory['stock_level'].isna())
    inventory['days_until_reorder'] = np.nan
    inventory.loc[mask, 'days_until_reorder'] = (
        inventory.loc[mask, 'stock_level'] / inventory.loc[mask, 'avg_daily_sales']
    ).round(1)

    # Drop only if critical columns are missing
    inventory = inventory.dropna(subset=['warehouse_id', 'product_id', 'stock_level', 
                                         'reorder_level', 'avg_daily_sales'])
    return inventory


def clean_sales(sales):
    sales = sales.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    sales = sales.drop_duplicates()
    sales = sales.dropna(subset=['sale_id', 'sale_date', 'product_id', 'customer_id', 'quantity', 'product_price'])
    # Ensure numeric for quantity and type to int
    sales['quantity'] = pd.to_numeric(sales['quantity'], errors='coerce')
    sales = sales.dropna(subset=['quantity'])
    sales['quantity'] = sales['quantity'].astype(int)
    # Ensure date format for sale_date
    sales['sale_date'] = pd.to_datetime(sales['sale_date'], format='%Y-%m-%d', errors='coerce')
    sales = sales.dropna(subset=['sale_date'])
    # Ensure numeric for product_price and total_sale_amount
    sales['product_price'] = pd.to_numeric(sales['product_price'], errors='coerce')
    sales['total_sale_amount'] = pd.to_numeric(sales['total_sale_amount'], errors='coerce')
    sales = sales.dropna(subset=['sale_id', 'sale_date', 'product_id', 'customer_id', 'quantity', 'product_price'])
    # Recalculate total_sale_amount with 2 decimal places
    sales['total_sale_amount'] = (sales['quantity'] * sales['product_price']).round(2)
    # Ensure Pattern for sale_id, customer_id, product_id
    sale__pattern = r'^S\d+$'
    customer_pattern = r'^C\d+$'
    product_pattern = r'^PID\d+$'
    sales = sales[
        sales['customer_id'].astype(str).str.match(customer_pattern) &
        sales['product_id'].astype(str).str.match(product_pattern) & 
        sales['sale_id'].astype(str).str.match(sale__pattern)
    ]
    return sales


# Saving cleaned data
def save_cleaned(products, customers, inventory, sales):
    output_dir = '.'  
    products.to_excel(os.path.join(output_dir, 'products_cleaned.xlsx'), index=False)
    customers.to_json(os.path.join(output_dir, 'customers_cleaned.json'), index=False)
    inventory.to_excel(os.path.join(output_dir, 'inventory_cleaned.xlsx'), index=False)
    sales.to_csv(os.path.join(output_dir, 'sales_cleaned.csv'), index=False)
    # so that can view cleaned data in csv format in vscode
    products.to_csv(os.path.join(output_dir, 'products_cleaned.csv'), index=False)
    customers.to_csv(os.path.join(output_dir, 'customers_cleaned.csv'), index=False)
    inventory.to_csv(os.path.join(output_dir, 'inventory_cleaned.csv'), index=False)

if __name__ == "__main__":
    products, customers, inventory, sales = load_data()
    eda_report(products, "Products")
    eda_report(customers, "Customers")
    eda_report(inventory, "Inventory")
    eda_report(sales, "Sales")
    products = clean_products(products)
    customers = clean_customers(customers)
    inventory = clean_inventory(inventory)
    sales = clean_sales(sales)
    save_cleaned(products, customers, inventory, sales)
    print("Data cleaning complete. Cleaned files saved in deliverables/.")
