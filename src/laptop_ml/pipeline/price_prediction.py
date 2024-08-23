from laptop_ml.config.configuration import ConfigurationManager
import joblib
import numpy as np


class PredictionPipeline:
    def __init__(self):
        self.config =ConfigurationManager().get_model_selection_config()

    def predict(self,df):
        model_path=self.config.model_path
        loaded_model=joblib.load(model_path)
        new_predictions=np.expm1(loaded_model.predict(df))

        return new_predictions