from laptop_ml.config.configuration import ConfigurationManager
from laptop_ml.components.missin_value_imputation import MissingValueImputation



class MissingValueImputationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        missing_value_config=config.get_missing_value_imputation_config()
        missing_value=MissingValueImputation(config=missing_value_config)
        missing_value.missing_value_imputation()