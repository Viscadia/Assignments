from enum import Enum

class DataVolume(Enum):
    NUM_PRODUCTS = 100
    NUM_CUSTOMERS = 1000
    NUM_DAYS = 150  # Number of days = number of sales workbooks
    MAX_VALID_SALES_RECORDS = 10_000_000
    INVENTORY_RECORDS = NUM_PRODUCTS * NUM_DAYS

class FileStructure(Enum):
    OUTPUT_FOLDER = "data"
    SALES_FOLDER = "sales"  # Folder inside OUTPUT_FOLDER for daily sales

class IssueRatios(Enum):
    DUPLICATE_PRODUCT_RATIO = 0.175
    MISSING_PRICE_RATIO = 0.125
    MISSPELLED_CATEGORY_RATIO = 0.10
    DUPLICATE_NAME_RATIO = 0.125
    REGION_MISSPELL_RATIO = 0.10
    INVALID_PRODUCT_ID_RATIO = 0.10
    INVALID_CUSTOMER_ID_RATIO = 0.10
    NEGATIVE_QUANTITY_RATIO = 0.05
    FUTURE_DATE_RATIO = 0.05
    NEGATIVE_STOCK_RATIO = 0.10
    NAN_STOCK_RATIO = 0.05
    FORMAT_ISSUE_RATIO = 0.10

class StaticLists(Enum):
    CATEGORIES = ["Antibiotic", "Analgesic", "Antiviral", "Antifungal", "Vaccine"]
    MISSPELLED_CATEGORIES = ["Antiboitic", "Analgisec", "Antyviral", "Antifangal", "Vacine"]
    REGION_MAP = {
        "North": "Noth", "South": "Suth", "East": "Eest", "West": "Wesst",
        "Central": "Cental", "Northeast": "N/E", "Southwest": "SWest"
    }
    SALES_REPS = [f"Rep_{i}" for i in range(1, 11)]
    SEGMENTS = ["Retail", "Hospital", "Online", "Wholesale"]
    CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
              "Delhi", "Bangalore", "Pune", "Zurich", "Basel"]
    STOCK_WORDS = ["twenty", "fifty", "one hundred", "zero", "ten", "fifteen"]
