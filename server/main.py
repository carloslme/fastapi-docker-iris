import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from classifier.iris_classifier import IrisClassifier as IrisClassifier
from models.models import Iris

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream

app = FastAPI()


@app.get("/")
def read_root():
    return "Iris classifier is all ready to go!"


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    logger.info("Servers is all ready to go!")
    return "Iris classifier is all ready to go!"


@app.post("/classify_iris")
async def classify(iris_features: Iris):
    logger.debug(f"Incoming iris features to the server: {iris_features}")
    iris_classifier = IrisClassifier()
    response = JSONResponse(iris_classifier.classify_iris(iris_features))
    logger.debug(f"Outgoing classification from the server: {response}")
    return response
