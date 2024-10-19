import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

class Model_Trainer():
    def __init__(self, data) -> None:
        self.data = data
        self.model = None
    
    def train_model(self):
        pass

    def test_model(self):
        pass