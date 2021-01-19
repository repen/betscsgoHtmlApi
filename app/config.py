import os

BASE_DIR = os.getenv("BASE_DIR", False)
PRODUCTION_WORK = os.getenv("EXTERNAL_WORK", False)
DATA_DIR = os.path.join( BASE_DIR, "data" ) if BASE_DIR else "/home/repente/prog/python/kwork/selenium/betcsgo/DockerApp/app/data"