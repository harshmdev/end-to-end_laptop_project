from laptop_ml.config.configuration import ConfigurationManager
from laptop_ml.components.model_selection import ModelSelection



class ModelSelectionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        model_selection_config=config.get_model_selection_config()
        featureselection=ModelSelection(config=model_selection_config)
        featureselection.train_model()