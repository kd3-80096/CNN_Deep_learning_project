from dataclasses import dataclass  #This will help us create same structure as above namedtuple
from pathlib import Path


@dataclass(frozen=True)  ## 
class DataIngestionConfig:
    root_dir: Path   ## here type will be path
    source_URL: str     ## here type will be 
    local_data_file: Path
    unzip_dir: Path