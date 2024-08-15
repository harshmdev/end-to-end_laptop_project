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