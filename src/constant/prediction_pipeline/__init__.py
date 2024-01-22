import os
from src.constant.s3_bucket import TRAINING_BUCKET_NAME

PRED_SCHEMA_FILE_PATH = os.path.join('config', 'prediction_schema.yaml')


PREDICTION_ARTIFACT_DIR_NAME ="prediction_artifacts"
PREDICTION_MODEL_STORE_DIR_NAME ="models"
PREDICTION_INPUT_FILE_NAME = "customer_pred_data.csv"
PREDICTION_OUTPUT_FILE_NAME = "customer_predictions.csv"
MODEL_BUCKET_NAME = TRAINING_BUCKET_NAME