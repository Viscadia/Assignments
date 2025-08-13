import pandas as pd
import glob
import os
#to extract data from files
class Extractor:
    def extract_sales(self, path):
        return pd.read_csv(path)

    def extract_products(self, path):
        return pd.read_excel(path)

    def extract_customers(self, path):
        return pd.read_json(path)

    def extract_inventory(self, path):
        return pd.read_excel(path)

class Transformer:
    def transform(self, sales, products, customers, inventory):
        # merge sales with products and customers
        df = sales.merge(products, on='product_id', how='left')
        df = df.merge(customers, on='customer_id', how='left')
        df = df.merge(inventory, on='product_id', how='left')
        return df

class Loader:
    def load(self, df, output_path):
        df.to_csv(output_path, index=False)

def main():
    extractor = Extractor()
    sales = extractor.extract_sales('sales_cleaned.csv')
    products = extractor.extract_products('products_cleaned.xlsx')
    customers = extractor.extract_customers('customers_cleaned.json')
    inventory = extractor.extract_inventory('inventory_cleaned.xlsx')

    transformer = Transformer()
    final_df = transformer.transform(sales, products, customers, inventory)
    
    # to save the final dataset 
    loader = Loader()
    loader.load(final_df, 'final_sales_dataset.csv')

if __name__ == '__main__':
    main()