import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read data from the Excel file
file_path = 'PowerBI_Data.xlsx'
data = pd.read_excel(file_path)

# Convert the Date column into Year, Month, Day columns
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Select feature columns and target column
features = ['CustomerID', 'ProductID', 'Quantity', 'Year', 'Month', 'Day']
target = 'TotalAmount'

X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Display the predicted results compared to actual values
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

# Predict future sales
future_data = {
    'CustomerID': [200, 201], # example future customer data
    'ProductID': [115, 116],
    'Quantity': [3, 4],
    'Year': [2024, 2024],
    'Month': [8, 8],
    'Day': [5, 6]
}
future_df = pd.DataFrame(future_data)
future_predictions = model.predict(future_df)
print(f'Future Predictions: {future_predictions}')
