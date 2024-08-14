from laptop_ml.constants import *
from laptop_ml.utils.common import read_yaml , create_directories
from laptop_ml.entity import DataGatheringConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH) :
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_gathering_config(self)->DataGatheringConfig:
        config=self.config.data_gathering
        create_directories([config.root_dir])

        data_gathering_config=DataGatheringConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file
        )

        return data_gathering_config