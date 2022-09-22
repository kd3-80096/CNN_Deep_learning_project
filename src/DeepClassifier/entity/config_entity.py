from dataclasses import (
    dataclass,
)  # This will help us create same structure as above namedtuple
from pathlib import Path


@dataclass(frozen=True)  ##
class DataIngestionConfig:
    root_dir: Path  ## here type will be path
    source_URL: str  ## here type will be
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


