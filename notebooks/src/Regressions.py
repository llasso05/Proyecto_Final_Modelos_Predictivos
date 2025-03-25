import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class RegressionEvaluator:

    def __init__(self, X, y, test_size=0.2, random_state=42):
        """
        Initialize the evaluator, training and test datasets
        """
        self.X_train, self.y_train, self.X_test, self.y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        self.models = {
            "Linear Regression": LinearRegression(),
            "Ridge Regression": Ridge(alpha=1.0),
            "Lasso Regression": Lasso(alpha=0.1),
            "Decission Tree": DecisionTreeRegressor(max_depth=5)
        }
        self.results=[]

    def train_and_evaluate(self):
        """
        Train and evaluate all models
        """
        for name, model in self.models.items():
            model.fit(self.X_train, self.y_train)
            y_pred = model.predict(self.X_test)
            mae = mean_absolute_error(self.y_test, y_pred)
            mse = mean_squared_error(self.y_test, y_pred)
            r2 = r2_score(self.y_test, y_pred)

            self.results.append({
                "Model": name, 
                "R2 Score": round(r2, 4),
                "RMSE": round(mse, 4),
                "MAE": round(mae, 4)
            })

    def print_results(self):
        """
        Prints evaluation results
        """
        results_df = pd.DataFrame(self.results)
        print(results_df)

