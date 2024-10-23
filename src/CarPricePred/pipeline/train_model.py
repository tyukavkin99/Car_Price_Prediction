from src.CarPricePred.components.data_ingestion import DataIngestion
from src.CarPricePred.components.data_transformation import DataTransformer
from src.CarPricePred.components.model_trainer import Model_Trainer
from sklearn import pipeline


def main():
    df = DataIngestion(file_path="../car_price_prediction_.csv").load_csv()
    df = DataTransformer(data=df).remove_id()
    pass

if __name__ == "main":
    main()