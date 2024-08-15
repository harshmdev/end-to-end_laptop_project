from laptop_ml.logging import logger
from laptop_ml.pipeline.stage_01_data_gathering import DataGatheringTrainingPipeline
from laptop_ml.pipeline.stage_02_data_ingestion_pipeline import DataIngestionTrainingPipeline
from laptop_ml.pipeline.stage_03_data_preprocessing_pipeline import DataPreprocessingPipeline

STAGE_NAME="Data Gathering"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_gathering=DataGatheringTrainingPipeline()
    data_gathering.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Ingestion"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_gathering=DataIngestionTrainingPipeline()
    data_gathering.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Preprocessing"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_gathering=DataPreprocessingPipeline()
    data_gathering.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e