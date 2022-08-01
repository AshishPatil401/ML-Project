from sklearn import pipeline
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

#schema_file_path = r"D:\ineuron\ML Modular Projects\ML-Project\config\schema.yaml"
#file_path = r"D:\ineuron\ML Modular Projects\ML-Project\housing\artifact\data_ingestion\2022-07-29-20-52-39\ingested_data\train\housing.csv"

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)

        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
