# Importing necessary modules
from dataclasses import dataclass
from pathlib import Path

# Defining a data class for storing data ingestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
 # Attribute annotations specify the data types
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path