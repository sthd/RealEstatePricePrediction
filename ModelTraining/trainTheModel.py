import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


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

def custom_train_test_split(ratio : float = 0.8):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 1-ratio, random_state=42)
    return X_train, X_test, y_train, y_test




if __name__ == '__main__':
    print("hi")
    X = np.random.rand(100, 2)
    y = np.random.rand(100)

X_train, X_test, y_train, y_test = custom_train_test_split()
print(f"{X_train} \n and \n {y_train}  \n and \n {X_test} \n and \n {y_test}")