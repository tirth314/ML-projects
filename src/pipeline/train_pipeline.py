import sys

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Training pipeline started")

            # 1. Data ingestion: read raw data, split into train/test
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

            # 2. Data transformation: build + fit preprocessing pipeline
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_tranformation(
                train_data_path, test_data_path
            )

            # 3. Model training: try multiple models, keep the best one
            model_trainer = ModelTrainer()
            r2_square, best_model = model_trainer.initiate_model_trainer(
                train_array=train_arr, test_array=test_arr
            )

            logging.info(
                f"Training pipeline completed. Best model: {best_model} | R2 score: {r2_square}"
            )
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainPipeline()
    score = pipeline.run_pipeline()
    print(f"Model trained successfully. R2 score: {score}")