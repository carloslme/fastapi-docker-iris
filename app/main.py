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
def predict_prod_iris_v1(input):
    url3 = "http://iris_classifier_v1_prod.docker:8000/prod/v1/classify_iris"
    logger.info("Prediction for Production Iris Classifier V1 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


def predict_prod_iris_v2(input):
    url3 = "http://iris_classifier_v2_prod.docker:8001/prod/v2/classify_iris"
    logger.info("Prediction for Production Iris Classifier V2 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


def predict_stag_iris_v1(input):
    url3 = "http://iris_classifier_v1_stag.docker:8002/stag/v1/classify_iris"
    logger.info("Prediction for Staging Iris Classifier V1 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


def predict_stag_iris_v2(input):
    url3 = "http://iris_classifier_v2_stag.docker:8003/stag/v2/classify_iris"
    logger.info("Prediction for Staging Iris Classifier V2 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


def predict_stag_iris_v3(input):
    url3 = "http://iris_classifier_v3_stag.docker:8004/stag/v3/classify_iris"
    logger.info("Prediction for Staging Iris Classifier V3 started")
    response = requests.post(url3, json=input)
    response = response.text

    return response


@app.get("/")
def read_root():
    logger.info("Front-end is all ready to go!")
    return "Front-end is all ready to go!"


@app.post("/prod/v1/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_prod_iris_v1(payload)
    return {"response": response}


@app.get("/prod/v1/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v1_prod.docker:8000/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.post("/prod/v2/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_prod_iris_v2(payload)
    return {"response": response}


@app.get("/prod/v2/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v2_prod.docker:8001/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.get("/stag/v1/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v1_stag.docker:8002/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.post("/stag/v1/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_stag_iris_v1(payload)
    return {"response": response}


@app.get("/stag/v2/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v2_stag.docker:8003/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.get("/stag/v3/healthcheck_iris")
async def v1_healhcheck():
    url3 = "http://iris_classifier_v3_stag.docker:8004/"

    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")

    return response


@app.post("/stag/v2/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_stag_iris_v2(payload)
    return {"response": response}


@app.post("/stag/v3/classify_iris")
def classify(payload: dict = Body(...)):
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_stag_iris_v3(payload)
    return {"response": response}
