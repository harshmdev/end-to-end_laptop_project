from src.laptop_ml.config.configuration import ConfigurationManager
from src.laptop_ml.components.feature_selection import FeatureSelection



class FeatureSelectionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        feature_selection_config=config.get_feature_selection_config()
        featureselection=FeatureSelection(config=feature_selection_config)
        featureselection.feature_selection()