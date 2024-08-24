from src.laptop_ml.config.configuration import ConfigurationManager
from src.laptop_ml.components.data_gathering import DataGathering



class DataGatheringTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_gathering_config=config.get_data_gathering_config()
        data_gathering=DataGathering(config=data_gathering_config)
        data_gathering.load_page()
        data_gathering.extract_html()
        data_gathering.close_driver()