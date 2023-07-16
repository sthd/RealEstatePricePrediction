import os

import numpy as np
import pickle
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




def custom_train_test_split(x, y, ratio : float = 0.8):
    checkInputType(ratio, float)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size= 1-ratio, random_state=42)
    return X_train, X_test, y_train, y_test

def saveToPikle(element, filename, overwrite=False):
        if os.path.exists(filename) and not overwrite:
            print(f"{filename} already exists. Element is not saved.")
            return

        with open(filename, 'wb') as file:
            pickle.dump(element, file)
        print(f"{filename} Element saved successfully.")

def loadFromPikle(filename):
    if os.path.exists(filename):
        # Load the elements from the file
        with open(filename, 'rb') as file:
            loaded_element = pickle.load(file)
            print(f"{filename} Element is loaded successfully.")
            return loaded_element
    else:
        print(f"{filename} does not exist. Element is not loaded.")



if __name__ == '__main__':
    print("hi")
    x = np.random.rand(100, 2)
    y = np.random.rand(100)

    X_train, X_test, y_train, y_test = custom_train_test_split(x, y)
    #print(f"{X_train} \n and \n {y_train}  \n and \n {X_test} \n and \n {y_test}")

    lr_model = MLModel("linear_regression")
    lr_model.train(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    print(f"original is {y_pred_lr}")
    rf_model = MLModel("random_forest")
    rf_model.train(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)


    element_filename_boolean_pairs = [
        (lr_model, "lr_model.pkl", True),
        (rf_model, "rf_model.pkl", False),
        ({"name": "John", "age": 30}, "file3.pkl", True)
    ]

    for element, filename, flag in element_filename_boolean_pairs:
        saveToPikle(element, filename, flag)

    loaded_model = loadFromPikle("lr_model.pkl")
    y_pred_lr = loaded_model.predict(X_test)
    print(f"loaded is {y_pred_lr}")
