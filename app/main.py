import logging
import requests

from fastapi import FastAPI, Body

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("frontend.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream

app = FastAPI()

# ML model prediction function using the prediction API request
def predict_iris_v1(input):
    url3 = "http://iris_classifier_v1.docker:8000/v1/classify_iris"
    logger.info("Prediction for Iris Classifier V1 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


def predict_iris_v2(input):
    url3 = "http://iris_classifier_v2.docker:8001/v2/classify_iris"
    logger.info("Prediction for Iris Classifier V2 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


@app.get("/")
def read_root():
    logger.info("Front-end is all ready to go!")
    return "Front-end is all ready to go!"


@app.post("/v1/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_iris_v1(payload)
    return {"response": response}


@app.get("/v1/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v1.docker:8000/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.post("/v2/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_iris_v2(payload)
    return {"response": response}


@app.get("/v2/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v2.docker:8001/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response
