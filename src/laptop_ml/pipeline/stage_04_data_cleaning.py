from laptop_ml.config.configuration import ConfigurationManager
from laptop_ml.components.data_cleaning import DataCleaning



class DataCleaningPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_cleaning_config=config.get_data_cleaning_config()
        data_cleaning=DataCleaning(config=data_cleaning_config)
        data_cleaning.data_cleaning()



