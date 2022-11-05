import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from classifier.iris_classifier_v1 import IrisClassifier as IrisClassifierV1
from models.models import Iris

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("prod_server_iris_classifier_v1.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream

app = FastAPI()


@app.get("/")
def read_root():
    return "Production Server Iris Classifier V1 is all ready to go!"


@app.get("/prod/healthcheck", status_code=200)
async def healthcheck():
    logger.info("Production Iris Classifier V1 is all ready to go!")
    return "Production Server Iris Classifier V1 is all ready to go!"


@app.post("/prod/v1/classify_iris")
async def classify(iris_features: Iris):
    logger.debug(
        f"Incoming iris features to the Production Iris Classifier V1: {iris_features}"
    )
    iris_classifier = IrisClassifierV1()
    response = JSONResponse(iris_classifier.classify_iris(iris_features))
    logger.debug(
        f"Outgoing classification from the Production Iris Classifier V1: {response}"
    )
    return response
