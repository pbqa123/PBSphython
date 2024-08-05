import matplotlib.pyplot as plt
import pandas as pd

# Creating sample data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Product_A': [150, 200, 250, 300, 350],
    'Product_B': [80, 100, 120, 140, 160],
    'Product_C': [200, 220, 240, 260, 280]
}

# Converting to DataFrame
df = pd.DataFrame(data)

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Product_A'], label='Product A', marker='o')
plt.plot(df['Month'], df['Product_B'], label='Product B', marker='s')
plt.plot(df['Month'], df['Product_C'], label='Product C', marker='^')
plt.title('Monthly Sales of Products')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(10, 6))
bar_width = 0.25
bar1 = range(len(df['Product_A']))
bar2 = [i + bar_width for i in bar1]
bar3 = [i + bar_width for i in bar2]

plt.bar(bar1, df['Product_A'], width=bar_width, label='Product A')
plt.bar(bar2, df['Product_B'], width=bar_width, label='Product B')
plt.bar(bar3, df['Product_C'], width=bar_width, label='Product C')
plt.title('Monthly Sales of Products')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks([r + bar_width for r in range(len(df['Month']))], df['Month'])
plt.legend()
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df['Product_A'], labels=df['Month'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution of Product A')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Product_A'], df['Product_B'], color='blue', label='Product A vs Product B')
plt.scatter(df['Product_A'], df['Product_C'], color='red', label='Product A vs Product C')
plt.title('Sales Comparison')
plt.xlabel('Product A Sales')
plt.ylabel('Other Products Sales')
plt.legend()
plt.grid(True)
plt.show()
