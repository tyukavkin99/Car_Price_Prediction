import pandas as pd
import numpy as np
from src.CarPricePred.exception import CustomException
from src.CarPricePred.logger import logging
import sys

class DataIngestion():
    def __init__(self, file_path=str()) -> pd.DataFrame:
        self.file_path = file_path
        self.data_frame = None

    def set_file_path(self,value=str()):
        self.file_path = value

    def get_file_path(self):
        return str(self.file_path)
    
    def load_csv(self):
        try:
            self.data_frame = pd.read_csv(self.file_path)
        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys)
        if self.data_frame != None:
            return self.data_frame