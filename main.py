from laptop_ml.logging import logger
from laptop_ml.pipeline.stage_01_data_gathering import DataGatheringTrainingPipeline
from laptop_ml.pipeline.stage_02_data_ingestion_pipeline import DataIngestionTrainingPipeline
from laptop_ml.pipeline.stage_03_data_preprocessing_pipeline import DataPreprocessingPipeline
from laptop_ml.pipeline.stage_04_data_cleaning import DataCleaningPipeline
from laptop_ml.pipeline.stage_05_missing_value_imputation import MissingValueImputationPipeline
from laptop_ml.pipeline.stage_06_feature_selection import FeatureSelectionPipeline
from laptop_ml.pipeline.stage_07_model_selection import ModelSelectionPipeline

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
    data_ingeation=DataIngestionTrainingPipeline()
    data_ingeation.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Preprocessing"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_preprocessing=DataPreprocessingPipeline()
    data_preprocessing.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Cleaning"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_cleaning=DataCleaningPipeline()
    data_cleaning.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Missing Value Imputation"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    missing_value=MissingValueImputationPipeline()
    missing_value.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Feature Selection"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    feature_selection=FeatureSelectionPipeline()
    feature_selection.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    model_training=ModelSelectionPipeline()
    model_training.main()
    logger.info(f"Finished>>>{STAGE_NAME}<<<Finished")
except Exception as e:
    logger.exception(e)
    raise e