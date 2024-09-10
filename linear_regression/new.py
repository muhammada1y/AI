import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Load dataset
s_data = pd.read_csv("score.csv")

# Show first 10 rows of the data
print(s_data.head(10))

# Define X and y (features and target)
X = s_data.iloc[:, :-1].values  # All rows, all columns except the last (features)
y = s_data.iloc[:, -1].values   # All rows, only the last column (target)

# Plot data
s_data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Scored')
plt.show()

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model using Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Fit the model
regressor.fit(X_train, y_train)
