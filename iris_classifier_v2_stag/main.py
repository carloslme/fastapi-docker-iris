import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from classifier.iris_classifier_v2 import IrisClassifier as IrisClassifierV2
from models.models import Iris

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("stag_server_iris_classifier_v2.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream

app = FastAPI()
iris_classifier_v2 = IrisClassifierV2()


@app.get("/")
def read_root():
    return "Staging Server Iris Classifier V2 is all ready to go!"


@app.get("/stag/v2/healthcheck", status_code=200)
async def healthcheck():
    logger.info("Staging Server Iris Classifier V2 is all ready to go!")
    return "Staging Server Iris Classifier V2 is all ready to go!"


@app.post("/stag/v2/classify_iris")
async def classify(iris_features: Iris):
    logger.debug(
        f"Incoming iris features to the Staging Iris Classifier V2: {iris_features}"
    )
    result = JSONResponse(iris_classifier_v2.classify_iris(iris_features))
    logger.debug(
        f"Outgoing classification from the Staging Iris Classifier V2: {result}"
    )
    return result


@app.on_event("startup")
async def startup():
    logger.info("Staging Server Iris Classifier V2 model is loaded")
    iris_classifier_v2.load_model()
