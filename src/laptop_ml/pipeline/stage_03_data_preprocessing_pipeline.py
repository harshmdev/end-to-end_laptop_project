from laptop_ml.config.configuration import ConfigurationManager
from laptop_ml.components.data_preprocessing import DataPreprocessing



class DataPreprocessingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_preprocessing_config=config.get_data_preprocessing_config()
        data_preprocessing=DataPreprocessing(config=data_preprocessing_config)
        data_preprocessing.data_preprocessing()
        data_preprocessing.export_preprocessed_data()



