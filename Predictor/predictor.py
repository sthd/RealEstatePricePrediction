from ModelTraining import trainTheModel as train
import numpy as np
#from sklearn.model_selection import train_test_split
from ModelTraining.trainTheModel import MLModel

"""
loaded is [0.5276654  0.51519511 0.52259891 0.49891022 0.49876531 0.47112677
 0.48360728 0.54573666 0.47577629 0.51314073 0.51300899 0.49898248
 0.47101056 0.47105366 0.48653274 0.49172951 0.46402446 0.48557033
 0.47504547 0.52027224]
 
 linear_regression_model.pkl Element is loaded successfully.
loaded is [0.47356995 0.53234302 0.45669603 0.47438359 0.46584401 0.52220567
 0.48946244 0.46491106 0.47452299 0.4479857  0.49845069 0.51607618
 0.51680063 0.49764975 0.49891665 0.49793302 0.4750782  0.44896659
 0.49944133 0.50007339]



hi
original is [0.53956307 0.52206865 0.57249735 0.55883298 0.54541319 0.51729697
 0.50053459 0.50845581 0.57183456 0.56249671 0.51653239 0.54271515
 0.53893694 0.55439169 0.54293668 0.5271677  0.50618106 0.55441501
 0.53762659 0.56460216]
linear_regression_model.pkl Element saved successfully.
linear_regression_model.pkl Element is loaded successfully.
loaded is [0.53956307 0.52206865 0.57249735 0.55883298 0.54541319 0.51729697
 0.50053459 0.50845581 0.57183456 0.56249671 0.51653239 0.54271515
 0.53893694 0.55439169 0.54293668 0.5271677  0.50618106 0.55441501
 0.53762659 0.56460216]

Process finished with exit code 0
 """


if __name__ == '__main__':
    print(f"hi")

    x = np.random.rand(100, 2)
    y = np.random.rand(100)

    X_train, X_test, y_train, y_test = train.custom_train_test_split(x, y)
    # print(f"{X_train} \n and \n {y_train}  \n and \n {X_test} \n and \n {y_test}")

    filename = '../ModelTraining/linear_regression_model.pkl'

    loaded_model = train.loadFromPikle(filename)

    y_pred_lr = loaded_model.predict(X_test)
    print(f"loaded is {y_pred_lr}")

