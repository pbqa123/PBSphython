import pandas as pd
import numpy as np
from scipy import stats

# Create sample data
data = {
    'Product_ID': range(1, 101),
    'Production_Time': np.random.normal(50, 10, 100),  # Normally distributed production time
    'Defect_Rate': np.random.normal(5, 2, 100),  # Normally distributed defect rate
    'Energy_Consumption': np.random.normal(200, 50, 100),  # Normally distributed energy consumption
    'Labor_Cost': np.random.normal(30, 5, 100)  # Normally distributed labor cost
}

# Introduce some random NaN values
for _ in range(10):
    data['Production_Time'][np.random.randint(0, 100)] = np.nan
    data['Defect_Rate'][np.random.randint(0, 100)] = np.nan
    data['Energy_Consumption'][np.random.randint(0, 100)] = np.nan
    data['Labor_Cost'][np.random.randint(0, 100)] = np.nan

df = pd.DataFrame(data)

# Save the initial data to a CSV file
df.to_csv('manufacturing_data.csv', index=False)

# Display initial data statistics
print("Initial Data Statistics:")
print(df.describe())

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Detect outliers using Z-score
z_scores = stats.zscore(df.select_dtypes(include=[np.number]))
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
df_cleaned = df[filtered_entries]

# Save the cleaned data to a CSV file
df_cleaned.to_csv('cleaned_manufacturing_data.csv', index=False)

# Display cleaned data statistics
print("Cleaned Data Statistics:")
print(df_cleaned.describe())
