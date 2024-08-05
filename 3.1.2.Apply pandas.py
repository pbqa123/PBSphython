import pandas as pd

file_path = 'PowerBI_Data.xlsx'
data = pd.read_excel(file_path, sheet_name=None)

# Hiển thị thông tin về các sheet trong file Excel
sheet_names = data.keys()
print("Sheet names:", sheet_names)

transactions_data = data['Transactions']
customers_data = data['Customers']
products_data = data['Products']
market_trends_data = data['MarketTrends']
website_access_data = data['WebsiteAccess']
categories_data = data['Categories']

#empty data handling
transactions_data.ffill(inplace=True)  # Fill blank values ​​with the value before
customers_data.bfill(inplace=True)     # Fill blank values ​​with the value after
products_data.dropna(axis=0, inplace=True)              # Remove rows containing blank values
market_trends_data.fillna(0, inplace=True)              # Fill blank values ​​with 0
website_access_data.dropna(axis=1, inplace=True)        # Remove columns containing blank values
categories_data.fillna('Unknown', inplace=True)         # Fill blank values ​​with 'Unknown'

# Handle empty data for each dataframe
transactions_data.dropna(inplace=True) # Remove rows containing empty values
customers_data.dropna(inplace=True) # Remove rows containing empty values
products_data.dropna(inplace=True) # Remove rows containing empty values
market_trends_data.dropna(inplace=True) # Remove rows containing empty values
website_access_data.dropna(inplace=True)# Remove rows containing empty values
categories_data.dropna(inplace=True) # Remove rows containing empty values

# #   Check for duplicate data
print("\nDuplicate rows in Transactions Data:", transactions_data.duplicated().sum())
print("Duplicate rows in Customers Data:", customers_data.duplicated().sum())
print("Duplicate rows in Products Data:", products_data.duplicated().sum())
print("Duplicate rows in Market Trends Data:", market_trends_data.duplicated().sum())
print("Duplicate rows in Website Access Data:", website_access_data.duplicated().sum())
print("Duplicate rows in Categories Data:", categories_data.duplicated().sum())


# In dữ liệu sau khi xử lý
print("Transactions Data:")
print(transactions_data.head())

print("\nCustomers Data:")
print(customers_data.head())

print("\nProducts Data:")
print(products_data.head())

print("\nMarket Trends Data:")
print(market_trends_data.head())

print("\nWebsite Access Data:")
print(website_access_data.head())

print("\nCategories Data:")
print(categories_data.head())

