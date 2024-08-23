from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataGatheringConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    html_file_path: Path
    data_path: Path

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    raw_data_path: Path
    preprocessed_data_path: Path

@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir: Path
    preprocessed_data_path: Path
    cleaned_data_path: Path

@dataclass(frozen=True)
class MissingValueImputationConfig:
    root_dir: Path
    after_cleaning: Path
    filled_data_path: Path

@dataclass(frozen=True)
class FeatureSelectionConfig:
    root_dir: Path
    after_missing_value_imputation: Path
    selected_data_path: Path

@dataclass(frozen=True)
class ModelSelectionConfig:
    root_dir: Path
    after_feature_selection: Path
    model_path: Path
    svr__C: int
    svr__gamma: str
    svr__kernel: str