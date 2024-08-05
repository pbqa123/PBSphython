import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# # Create sample data
np.random.seed(0)
X = 2.5 * np.random.randn(100) + 1.5
y = 2 * X + np.random.randn(100)

# Convert data to DataFrame
df = pd.DataFrame({'X': X, 'y': y})

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(df[['X']], df['y'], test_size=0.2, random_state=0)

# Initialize linear regression model
model = LinearRegression()

# Model training
model.fit(X_train, y_train)

# Prediction on test set
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Draw a chart
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
