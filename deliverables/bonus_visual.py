import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading final sales dataset (after ETL)
df = pd.read_csv('final_sales_dataset.csv')

# Filtering for last 2 months
df['sale_date'] = pd.to_datetime(df['sale_date'])
last_2_months = df['sale_date'] >= (df['sale_date'].max() - pd.DateOffset(months=2))
df_recent = df[last_2_months]

# Aggregate sales
grouped = df_recent.groupby(['region', 'product_id', 'product_name'])['quantity'].sum().reset_index()

# for top 3 products per region
grouped['rank'] = grouped.groupby('region')['quantity'].rank(method='first', ascending=False)
top3 = grouped[grouped['rank'] <= 3]

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=top3, x='region', y='quantity', hue='product_name')
plt.title('Top 3 Selling Products per Region (Last 2 Months)')
plt.ylabel('Total Quantity Sold')
plt.xlabel('Region')
plt.legend(title='Product')
plt.tight_layout()
plt.show()
