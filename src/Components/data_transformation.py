import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging


@dataclass()
class DataTransformationConfig:
    preprocessor_obj_file = os.path.join('artifact', "preprocessor.pkl")


class DataTransforation:
    def __int__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):

        try:
            numerical_columns = ["writing_score", "reading_socre"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler()),
                ]
            )

            logging.info("Imputing and Scaling complete for numerical columns")
            logging.info("Imputing, OneHotEncoding and Scaling complete for categorical columns")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_columns)
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self,train_path,test_path):
