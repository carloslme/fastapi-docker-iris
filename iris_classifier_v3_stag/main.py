import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from classifier.iris_classifier_v3 import IrisClassifier as IrisClassifierV3
from models.models import Iris

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("stag_server_iris_classifier_v3.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream

app = FastAPI()
iris_classifier_v3 = IrisClassifierV3()


@app.get("/")
def read_root():
    return "Staging Server Iris Classifier V3 is all ready to go!"


@app.get("/stag/v3/healthcheck", status_code=200)
async def healthcheck():
    logger.info("Staging Server Iris Classifier V3 is all ready to go!")
    return "Staging Server Iris Classifier V3 is all ready to go!"


@app.post("/stag/v3/classify_iris")
async def classify(iris_features: Iris):
    logger.debug(
        f"Incoming iris features to the Staging Iris Classifier V3: {iris_features}"
    )
    result = JSONResponse(iris_classifier_v3.classify_iris(iris_features))
    logger.debug(
        f"Outgoing classification from the Staging Iris Classifier V3: {result}"
    )
    return result


@app.on_event("startup")
async def startup():
    logger.info("Staging Server Iris Classifier V3 model is loaded")
    iris_classifier_v3.load_model()
