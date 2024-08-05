# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Step 2: Prepare the data
# Create sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Convert to DataFrame for better data manipulation
df = pd.DataFrame(data=np.hstack((X, y)), columns=['Feature', 'Target'])

# Step 3: Data Preprocessing
# Check for missing values
if df.isnull().sum().sum() > 0:
    df = df.dropna()

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Feature']])
y_scaled = scaler.fit_transform(df[['Target']])

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Step 5: Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R^2 Score:", r2)

# Display the regression coefficients and intercept
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

