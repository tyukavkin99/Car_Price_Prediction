import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


class DataHandler(object):

    def __init__(self, data: np.array) -> None:
        self.data = data

    def get_dataframe(self):
        pass