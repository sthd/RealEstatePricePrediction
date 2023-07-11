from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score





class ModelEvaluator:
    def __init__(self, y_test, y_pred):
        #self.algorithm = "model"
        self.y_test = y_test
        self.y_pred = y_pred
        self.mse = None
        self.mae = None
        self.r2 = None
    # Evaluation metrics for Linear Regression and Random Forest
    def evaluate(self):
        self.mse = mean_squared_error(self.y_test, self.y_pred)
        self.mae = mean_absolute_error(self.y_test, self.y_pred)
        self.r2 = r2_score(self.y_test, self.y_pred)

        return self.mse, self.mae, self.r2

    def printEvaluations(self, algorithm : str ="model"):
        if self.mse is None or self.mae is None or self.r2 is None:
            self.evaluate()
        print(f"{algorithm} predictions: {self.y_pred}, MSE: {self.mse}, MAE: {self.mae}, R2: {self.r2}")




if __name__ == '__main__':
    y_test = [0, 1.1, 3]
    y_pred = [0, 1, 2]
    evaluator = ModelEvaluator(y_test, y_pred)
    evaluator.printEvaluations("lin")
