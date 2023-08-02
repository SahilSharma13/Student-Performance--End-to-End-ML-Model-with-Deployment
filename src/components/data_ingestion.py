import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dateclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str.os.path.join('artifacts',"train.csv")
    test_data_path: str.os.path.join('artifacts',"test.csv")
    raw_data_path: str.os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.inf("Entered the data ingestion method or component")
        try:
            def=pd.read_csv('')
        except:
            pass