# Importing the os module for interacting with the operating system
import os

# Importing BoxValueError from box.exceptions for handling specific exceptions related to Box operations
from box.exceptions import BoxValueError

# Importing the yaml module for working with YAML files
import yaml

# Importing the logger object from cnnClassifier for logging messages
from Chest_Cancer_Classification import logger

# Importing the json module for working with JSON data
import json

# Importing joblib for saving and loading Python objects (e.g., models) efficiently
import joblib

# Importing ensure_annotations from the ensure library for ensuring function annotations
from ensure import ensure_annotations

# Importing ConfigBox from the box module for enhanced dictionary-like configuration handling
from box import ConfigBox

# Importing Path from pathlib for object-oriented filesystem paths
from pathlib import Path

# Importing Any from the typing module for type hinting any type
from typing import Any

# Importing base64 for encoding and decoding data in Base64 format
import base64

# Function to read a YAML file and return its content as a ConfigBox for easy attribute access
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

# Function to create multiple directories at specified paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# Function to save data to a JSON file for structured and human-readable storage
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")



# Function to load data from a JSON file and return it as a ConfigBox for easy attribute access
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

# Function to save data to a binary file for efficient storage and retrieval of large objects
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

# Function to load data from a binary file for efficient retrieval of large objects
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

# Function to get the size of a file in KB for reporting and monitoring purposes
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

# Function to decode a base64-encoded image string and save it to a file for image processing or storage
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

# Function to encode an image file into a base64 string for easy transmission or embedding in web pages
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())