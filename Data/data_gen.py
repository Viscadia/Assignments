import os
import csv
import json
import math
import random
import numpy as np
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
from concurrent.futures import ProcessPoolExecutor
from enum_config import DataVolume, FileStructure, IssueRatios, StaticLists

# Setup
fake = Faker()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, FileStructure.OUTPUT_FOLDER.value)
SALES_DIR = os.path.join(OUTPUT_DIR, FileStructure.SALES_FOLDER.value)

os.makedirs(SALES_DIR, exist_ok=True)

# Output files
PRODUCTS_FILE = os.path.join(OUTPUT_DIR, "products.csv")
CUSTOMERS_FILE = os.path.join(OUTPUT_DIR, "customers.json")
INVENTORY_FILE = os.path.join(OUTPUT_DIR, "inventory.csv")

# Helper data
categories = StaticLists.CATEGORIES.value
misspelled_categories = StaticLists.MISSPELLED_CATEGORIES.value
region_map = StaticLists.REGION_MAP.value
regions = list(region_map.keys())
sales_reps = StaticLists.SALES_REPS.value
segments = StaticLists.SEGMENTS.value
cities = StaticLists.CITIES.value
stock_words = StaticLists.STOCK_WORDS.value

valid_product_ids = [f"PID{1000 + i}" for i in range(DataVolume.NUM_PRODUCTS.value)]
valid_customer_ids = [f"C{1000 + i}" for i in range(DataVolume.NUM_CUSTOMERS.value)]
product_price_map = {pid: round(random.uniform(5, 100), 2) for pid in valid_product_ids}

# 1. Generate Products
def generate_products():
    products = []
    for i in range(DataVolume.NUM_PRODUCTS.value):
        products.append({
            "product_id": f"PID{1000 + i}",
            "product_name": f"Drug_{i}",
            "category": random.choice(categories),
            "price": round(random.uniform(5, 100), 2)
        })

    for idx in random.sample(range(len(products)), math.floor(IssueRatios.MISSING_PRICE_RATIO.value * len(products))):
        products[idx]["price"] = ""

    for idx in random.sample(range(len(products)), math.floor(IssueRatios.MISSPELLED_CATEGORY_RATIO.value * len(products))):
        cat = products[idx]["category"]
        if cat in categories:
            products[idx]["category"] = misspelled_categories[categories.index(cat)]

    pd.DataFrame(products).to_csv(PRODUCTS_FILE, index=False)

# 2. Generate Customers
def generate_customers():
    customers = []
    for i in range(DataVolume.NUM_CUSTOMERS.value):
        customers.append({
            "customer_id": f"C{1000 + i}",
            "customer_name": fake.name(),
            "type": random.choice(segments),
            "city": random.choice(cities),
            "region": random.choice(regions),
            "sales_rep": random.choice(sales_reps)
        })

    for idx in random.sample(range(len(customers)), math.floor(IssueRatios.REGION_MISSPELL_RATIO.value * len(customers))):
        reg = customers[idx]["region"]
        customers[idx]["region"] = region_map.get(reg, reg)

    for idx in random.sample(range(len(customers)), math.floor(IssueRatios.DUPLICATE_NAME_RATIO.value * len(customers))):
        source_idx = random.choice([i for i in range(len(customers)) if i != idx])
        customers[idx]["customer_name"] = customers[source_idx]["customer_name"]

    with open(CUSTOMERS_FILE, "w") as f:
        json.dump(customers, f, indent=2)

# 3. Generate Sales - Parallelized
def generate_sales_day(day_index):
    today = datetime(2023, 1, 1) + timedelta(days=day_index)
    rows = []
    records_per_day = math.ceil(DataVolume.MAX_VALID_SALES_RECORDS.value / DataVolume.NUM_DAYS.value)
    global_counter_start = day_index * records_per_day + 1

    for i in range(records_per_day):
        pid = random.choice(valid_product_ids)
        cid = random.choice(valid_customer_ids)
        qty = random.randint(1, 20)
        price = product_price_map.get(pid, round(random.uniform(10, 100), 2))
        total = round(price * qty, 2)
        rows.append([
            f"S{global_counter_start + i:08d}",
            today.strftime("%Y-%m-%d"),
            pid,
            cid,
            qty,
            price,
            total
        ])

    for _ in range(random.randint(1000, 5000)):
        rows.append(["", "", f"INVALID_{random.randint(9000,9999)}", f"Z{random.randint(9000,9999)}",
                     random.choice([None, -10, 0]), None, None])

    df = pd.DataFrame(rows, columns=[
        "sale_id", "sale_date", "product_id", "customer_id",
        "quantity", "product_price", "total_sale_amount"
    ])
    df.to_excel(os.path.join(SALES_DIR, f"sales_day_{day_index+1:03}.xlsx"), index=False)
    return day_index + 1

# 4. Generate Inventory
def generate_inventory():
    inventory_rows = []
    for day in range(DataVolume.NUM_DAYS.value):
        for i in range(DataVolume.NUM_PRODUCTS.value):
            pid = valid_product_ids[i]
            avg_daily_sales = random.randint(10, 100)
            stock_level = int(avg_daily_sales * random.uniform(1.2, 2.0))
            days_until_reorder = round(stock_level / avg_daily_sales, 1)
            inventory_rows.append({
                "warehouse_id": f"W{day:03}_{i:03}",
                "product_id": pid,
                "stock_level": stock_level,
                "reorder_level": random.randint(20, 100),
                "avg_daily_sales": avg_daily_sales,
                "days_until_reorder": days_until_reorder
            })

    for idx in random.sample(range(len(inventory_rows)), math.floor(IssueRatios.NAN_STOCK_RATIO.value * len(inventory_rows))):
        inventory_rows[idx]["stock_level"] = np.nan
    for idx in random.sample(range(len(inventory_rows)), math.floor(IssueRatios.NEGATIVE_STOCK_RATIO.value * len(inventory_rows))):
        inventory_rows[idx]["stock_level"] = -random.randint(1, 100)
    for idx in random.sample(range(len(inventory_rows)), math.floor(IssueRatios.FORMAT_ISSUE_RATIO.value * len(inventory_rows))):
        inventory_rows[idx]["stock_level"] = random.choice(stock_words)

    pd.DataFrame(inventory_rows).to_csv(INVENTORY_FILE, index=False)

# Main
if __name__ == "__main__":
    generate_products()
    generate_customers()

    with ProcessPoolExecutor() as executor:
        list(executor.map(generate_sales_day, range(DataVolume.NUM_DAYS.value)))

    generate_inventory()
    print("✅ Data generation complete.")
