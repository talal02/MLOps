# Import necessary libraries
from flask import Flask
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

app = Flask(__name__)

# # Load dataset from CSV file
# df = pd.read_csv('Salary_Data.csv')

# # Split data into input and output variables
# X = df.iloc[:, :-1].values
# y = df.iloc[:, -1].values

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Train linear regression model
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)

# # Predict salaries on test set
# y_pred = regressor.predict(X_test)

# # Print model coefficients and accuracy
# print("Coefficients:", regressor.coef_)
# print("Intercept:", regressor.intercept_)
# print("Accuracy:", regressor.score(X_test, y_test))

@app.route('/')
def home():
    return "WELCOME TO MY APP"

# @app.route('/predict/<years_of_experience>')
# def predict(years_of_experience):
#     years_of_experience = float(years_of_experience)
#     predicted_salary = regressor.predict([[years_of_experience]])
#     print("Predicted salary for %0.1f years of experience: $%0.2f" % (years_of_experience, predicted_salary[0]))
#     return str(predicted_salary[0])

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')