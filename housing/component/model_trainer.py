from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import ModelTrainerConfig
from housing.entity.artifact_entity import DataTransformationArtifact
from housing.util.util import read_yaml_file,save_object, load_numpy_array, load_data

import os,sys
import numpy as np
import pandas as pd

from housing.entity import model_factory

# Steps
# 1. loading transformed training and testing datset
# 2. reading model config file 
# 3. getting best model on training datset
# 4. evaludation models on both training & testing datset -->model object
# 5. loading preprocessing pbject
# 6. custom model object by combining both preprocessing obj and model obj
# 7. saving custom model object
# 8. return model_trainer_artifact




class ModelTrainer:


    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info(f"{'>>'*15}Model Trainer log started.{'<<'*15}")            
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact =data_transformation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_trainer(self):
        try:
            logging.info(f"Loading transformed training dataset in numpy array format")
            transformed_train_file_path = self.data_transformation_artifact.transformed_train_file_path
            train_array = load_numpy_array(file_path=transformed_train_file_path)

            logging.info(f"Loading transformed testing dataset in numpy array format")
            transformed_test_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = load_numpy_array(file_path=transformed_test_file_path)

            logging.info(f"Splitting training and testing dataset")
            x_train,y_train,x_test,y_test = train_array[:,:-1],train_array[:,-1], test_array[:,:-1], test_array[:,-1]

            logging.info(f"Extracting model config file path")
            model_config_file_path = self.model_trainer_config.model_config_file_path

            logging.info(f"Initializing model factory class using above model config file path")
            model_factory = ModelFactory()

            base_accuracy = self.model_trainer_config.base_accuracy
            logging.info(f"Expected accuracy: {base_accuracy}")

            logging.info(f"Initiating operation model selection")








        except Exception as e:
            raise HousingException(e,sys) from e
    
