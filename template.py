import os  # Import the os module to interact with the operating system
from pathlib import Path  # Import Path from pathlib to handle file paths
import logging  # Import logging to log messages

# Configure logging to display the time and the message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "Chest-Cancer-Classification"

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # .gitkeep file to ensure the directory is tracked by git
    f"src/{project_name}/__init__.py",  # __init__.py to make this directory a package
    f"src/{project_name}/components/__init__.py",  # __init__.py for components package
    f"src/{project_name}/utils/__init__.py",  # __init__.py for utils package
    f"src/{project_name}/config/__init__.py",  # __init__.py for config package
    f"src/{project_name}/config/configuration.py",  # configuration.py file in config package
    f"src/{project_name}/pipeline/__init__.py",  # __init__.py for pipeline package
    f"src/{project_name}/entity/__init__.py",  # __init__.py for entity package
    f"src/{project_name}/constants/__init__.py",  # __init__.py for constants package
    "config/config.yaml",  # YAML file for configuration
    "dvc.yaml",  # DVC configuration file
    "params.yaml",  # Parameters configuration file
    "requirements.txt",  # Requirements file for dependencies
    "setup.py",  # Setup script for the project
    "research/trials.ipynb",  # Jupyter notebook for research
    "templates/index.html"  # HTML file for templates
]

# Loop through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the string path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and file name

    # If the directory part of the path is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Log directory creation

    # If the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create an empty file
            pass  # No need to write anything
            logging.info(f"Creating empty file: {filepath}")  # Log file creation

    else:
        logging.info(f"{filename} already exists")  # Log if the file already exists
