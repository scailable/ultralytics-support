"""
This script downloads a specific version of a dataset from Roboflow using the Roboflow API.
Modules:
    roboflow: A module to interact with the Roboflow API.
    os: A module to interact with the operating system, used here to get environment variables.
Environment Variables:
    ROBOFLOW_API_KEY: The API key for authenticating with the Roboflow API. This must be set in the environment.
Raises:
    Exception: If the ROBOFLOW_API_KEY environment variable is not set.
Usage:
    Ensure the ROBOFLOW_API_KEY environment variable is set to your Roboflow API key.
    Run the script to download the specified version of the dataset in YOLOv11 format.
"""
from os import getenv
from roboflow import Roboflow
from os.path import *

try:
    ROBOFLOW_API_KEY = getenv("ROBOFLOW_API_KEY")
    if not ROBOFLOW_API_KEY:
        raise Exception("ROBOFLOW_API_KEY not set.")
except:
    raise Exception("Please set the environment variable ROBOFLOW_API_KEY to your Roboflow API key.")

# get current directory
current_dir = dirname(realpath(__file__))

rf = Roboflow(api_key=ROBOFLOW_API_KEY)
project = rf.workspace("egg-detection-mixed-eggs").project("egg-detection-model-4wo1k")
version = project.version(3)
dataset = version.download("yolov11", location=join(current_dir, "eggs-dataset"))