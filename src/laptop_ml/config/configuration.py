from laptop_ml.constants import *
from laptop_ml.utils.common import read_yaml , create_directories
from laptop_ml.entity import DataGatheringConfig , DataIngestionConfig , DataPreprocessingConfig , DataCleaningConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH) :
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_gathering_config(self)->DataGatheringConfig:
        config=self.config.data_gathering
        create_directories([config.root_dir])

        data_gathering_config=DataGatheringConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file
        )

        return data_gathering_config
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            html_file_path=config.html_file_path,
            data_path=config.data_path

        )

        return data_ingestion_config
    
    def get_data_preprocessing_config(self)->DataPreprocessingConfig:
        config=self.config.data_preprocessing
        create_directories([config.root_dir])

        data_preprocessing_config=DataPreprocessingConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
            preprocessed_data_path=config.preprocessed_data_path
        )

        return data_preprocessing_config
    
    def get_data_cleaning_config(self)->DataCleaningConfig:
        config=self.config.data_cleaning
        create_directories([config.root_dir])

        data_cleaning_config=DataCleaningConfig(
            root_dir=config.root_dir,
            preprocessed_data_path=config.preprocessed_data_path,
            cleaned_data_path=config.cleaned_data_path
        )
        return data_cleaning_config