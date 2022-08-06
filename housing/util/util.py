import yaml
from housing.exception import HousingException
import os, sys
import numpy as np
import pandas as pd
import dill
from housing.constant import *


def write_yaml_file(file_path:str, data:dict):
    """
    Description: Create a yaml file
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e


def read_yaml_file(file_path:str) -> dict:
    """
    Description: Read a yaml file and returns the content as a dictionary
    file_path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e


def save_numpy_array_data(file_path:str,array:np.array):
    try:
        """
        Description: Save numpy array data to file.
        file_path: str location of file to store.
        array: np.array data to store
        """
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise HousingException(e,sys) from e


def load_numpy_array(file_path:str)-> np.array:
    try:
        """
        Description: Load numpy array data to file.
        file_path: str location of file to read.
        return: np.array data loaded.
        """
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e


def save_object(file_path:str,obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e


def load_object(file_path:str):
    try:
        """
        file_path: str
        """
        dir_path = os.path.dirname(file_path)
        with open(file_path, "rb") as file_obj:
            dill.load(file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e



def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
            
        dataframe = pd.read_csv(file_path)

        error_message = ""

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message = f"{error_message} Column: [{column}] is not in schema."
        if len(error_message)>0:
            raise Exception(error_message)
            
        return dataframe
    except Exception as e:
        raise HousingException(e,sys) from e
