from build.lib import src
from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException
from src.mlproject2.components.data_ingestion import DataIngestion
from src.mlproject2.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("Starting the application...")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("custom exception is being raised")
        raise CustomException(e,sys)