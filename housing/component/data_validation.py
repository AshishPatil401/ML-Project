from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.util.util import read_yaml_file
from constant import *
import os,sys
import pandas as pd

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json


class DataValidation:
    
    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact
    ) -> None:
        try:
            logging.info(f"{'>>'*15}Data Valdaition log started.{'<<'*15}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise HousingException(e,sys) from e


    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info("Checking whether training and testing files are available")
            is_train_file_exists = False
            is_test_file_exists = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)

            is_available = is_train_file_exists and is_test_file_exists

            logging.info(f"Is train and Test files exits? -> [{is_available}]")

            if not is_available:
                train_file = self.data_ingestion_artifact.train_file_path
                test_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file : {train_file} or Testing file : {test_file} is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e


    def validate_dataset_schema(self) -> bool:
        try:
            logging.info("Checking whether training and testing data file are valid or not")
            validation_status = False
            
            """
            Assignment:
                1.Number of columns
                2.Column names
                3.Ocean proximity check values
                    acceptable values:INLAND, ISLAND, NEAR_BAY, NEAR_OCEAN
            """
            
            # Read schema info
            schema_info = read_yaml_file(self.data_validation_config.schema_file_path)
            schema_columns = list(schema_info[DATASET_SCHEMA_COLUMNS_KEY].keys())
            schema_domain_values = list(schema_info[DOMAIN_VALUE_KEY][OCEAN_PROXIMITY_KEY])
            schema_number_of_columns = len(schema_columns)

            # Read train and test file
            train_df,test_df = self.get_train_and_test_df()

            # Train file info
            train_columns = list(train_df.columns)
            train_number_of_columns = len(train_columns)
            train_domain_values = list(train_df["ocean_proximity"].value_counts().index)

            # Test file info
            test_columns = list(test_df.columns)
            test_number_of_columns = len(test_columns)
            test_domain_values = list(test_df["ocean_proximity"].value_counts().index)

            # 1.Check number of columns
            is_number_of_column_match = False
            if (schema_number_of_columns==train_number_of_columns) and (schema_number_of_columns==test_number_of_columns):
                is_number_of_column_match = True
                logging.info(f"Is number of columns match? -> [{is_number_of_column_match}]")
            else:
                raise Exception("Input number of columns number does not match with schema")

            # 2.Check column names
            is_column_name_match = False
            schema_columns.sort()
            train_columns.sort()
            test_columns.sort()
            if(schema_columns==train_columns)and(schema_columns==test_columns):
                is_column_name_match = True
                logging.info(f"Is column names match? -> [{is_column_name_match}]")
            else:
                raise Exception("Input columns names does not match with schema")

            # 3.Ocean proximity check values
            is_domain_values_match = False
            schema_domain_values.sort()
            train_domain_values.sort()
            test_domain_values.sort()

            if(schema_domain_values==train_domain_values)and(schema_domain_values==test_domain_values):
                is_domain_values_match = True
                logging.info(f"Is schema domain values for ocean_proximity match? -> [{is_domain_values_match}]")
            else:
                raise Exception("ocean_proximity values does not match with schema")

            validation_status = is_number_of_column_match and is_column_name_match and is_domain_values_match
            
            logging.info(f"Data Validation status? -> [{validation_status}]")
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])
            
            train_df, test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path, "w") as report_file:
                json.dump(report, report_file, indent=6)

            return report
        except Exception as e:
            raise HousingException(e,sys) from e


    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise HousingException(e,sys) from e 


    def is_data_drift_found(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e



    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path = self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successfully..."
            )
            logging.info(f"Data validation artifact : {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    
    def __del__(self):
        logging.info(f"{'>>'*15}Data Valdaition log completed.{'<<'*15} \n  ")
