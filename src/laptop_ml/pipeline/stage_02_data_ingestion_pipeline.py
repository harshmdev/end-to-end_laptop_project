from src.laptop_ml.config.configuration import ConfigurationManager
from src.laptop_ml.components.data_ingestion import DataIngestion



class DataGatheringTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.read_html()
        data_ingestion.data_extractor()
        data_ingestion.convert_to_df()
        data_ingestion.export_df()