import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

class Model_Trainer():
    def __init__(self, model, train_data, test_data=None) -> None:
        self.train_data = train_data
        self.test_data = test_data
        self.model = model
    
    def fit_data(self):
        self.fit_model = self.model.fit(self.test_data)
        return self.fit_model
    
    def test_model(self):
        y = self.fit_model.predict(self.test_data)
        return y