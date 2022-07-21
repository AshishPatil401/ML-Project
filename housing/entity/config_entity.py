from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url",
                                                        "tgz_download_dir",
                                                        "raw_data_dir",
                                                        "ingested_train_dir",
                                                        "ingested_test_dir"])

DataValidationConfig = namedtuple("Datavalidation_config",["schema_file_patih"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                  "transformed_train_dir",
                                                                  "transformed_test_dir",
                                                                  "preprocessed_object_file_path"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig", ["trained_model_file_path","base_accuraccy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])
