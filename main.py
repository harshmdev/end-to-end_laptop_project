from laptop_ml.logging import logger
from laptop_ml.pipeline.stage_01_data_gathering import DataGatheringTrainingPipeline

STAGE_NAME="Data Gathering"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_gathering=DataGatheringTrainingPipeline()
    data_gathering.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e