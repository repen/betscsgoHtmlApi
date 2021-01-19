import os

BASE_DIR = os.getenv("BASE_DIR", os.getcwd())
PRODUCTION_WORK = os.getenv("EXTERNAL_WORK", False)
DATA_DIR = os.getenv("DATA_DIR",  "/home/repente/prog/python/kwork/selenium/betcsgo/DockerApp/app/data" )