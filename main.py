from MLproject import logger
from MLproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>> stage {STAGE_NAME} started>>")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>> stage{STAGE_NAME} completed<<<")
    
except Exception as e:
    logger.exception(e)
    raise e