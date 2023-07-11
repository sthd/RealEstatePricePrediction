import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def checkInputType(input, expected_type):
    if isinstance(input, expected_type):
        return True
    else:
        raise TypeError(f"Invalid data type. Expected {expected_type}.")

class MLModel:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.model = None

    def train(self, X_train, y_train):
        if self.algorithm == 'linear_regression':
            self.model = LinearRegression()
        elif self.algorithm == 'random_forest':
            self.model = RandomForestRegressor()

        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

def custom_train_test_split(ratio : float = 0.8):
    checkInputType(ratio, float)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 1-ratio, random_state=42)
    return X_train, X_test, y_train, y_test




if __name__ == '__main__':
    print("hi")
    X = np.random.rand(100, 2)
    y = np.random.rand(100)

X_train, X_test, y_train, y_test = custom_train_test_split()
print(f"{X_train} \n and \n {y_train}  \n and \n {X_test} \n and \n {y_test}")

lr_model = MLModel("linear_regression")
lr_model.train(X_train, y_train)

y_pred_linear_regression = lr_model.predict(X_test)

rf_model = MLModel("random_forest")
rf_model.train(X_train, y_train)
y_pred_random_forest = rf_model.predict(X_test)