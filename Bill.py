# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:54:01 2023

@author: drish
"""
from sklearn.linear_model import LinearRegression
import pandas as pd
# Step 1: Read the CSV file
dataset = pd.read_csv("form.csv")

# Step 2: Extract features (x) and target (y)
y = dataset["electricity bill"]
x = dataset[["AC", "TV", "fridge"]]

# Step 3: Create and train the linear regression model
model = LinearRegression()
model.fit(x, y)

# Step 4: Create a function to take user input and predict the output
def predict_profit():
    print("Enter the following information:")
    rd_spend = float(input("AC hours: "))
    administration = float(input("TV hours: "))
    marketing_spend = float(input("fridge hours: "))

    # Create a dataframe with the input values
    input_data = pd.DataFrame({
        'AC': [rd_spend],
        'TV': [administration],
        'fridge': [marketing_spend]
    })

    # Use the model to predict the output
    predicted_profit = model.predict(input_data)

    print(f"Predicted bill: {predicted_profit[0]:.2f}")

# Step 5: Call the function to get predictions from user input
predict_profit()