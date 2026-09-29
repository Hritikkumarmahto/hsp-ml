import os
from pathlib import Path
import mlflow
import mlflow.sklearn

import pandas as pd

from fastapi import FastAPI

from fastapi.responses import FileResponse

from fastapi .staticfiles import StaticFiles
from pydantic import BaseModel,Field

BASE_DIR=Path(__file__).resolve().parent()
TRACKING_URI=os.getenv("MLFLOW_TRACKING","https://127.0.0.1:5000")