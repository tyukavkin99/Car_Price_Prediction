import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder

class DataTransformer():
    def __init__(self, data:pd.DataFrame, train_data=None) -> None:
        self.data = data
        self.train_data = None

    def remove_id(self):
        self.data = self.data.drop(cols=['Car ID'])

    def transform_onehot(self, data):
        if self.train_data == True:
            enc = OneHotEncoder(handle_unknown=True)
            enc = enc.fit(data)
            with open("encoder.pkl", "wb") as f:
                pickle.dump(enc, f)
            trans_data = enc.transform(data)
            return trans_data
        else:
            with open("encoder.pkl", "r") as f:
                enc = pickle.load(f)


