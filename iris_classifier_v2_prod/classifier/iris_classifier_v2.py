import joblib
import logging
import sys

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from models.models import Iris

sys.path.append("..")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("prod_iris_classifier_v2.log")
file_handler.setFormatter(formatter)

# THIS IS THE NEW CHANGE TO STREAM LOGS
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        logger.info("Data Production Iris Classifier V2 loaded")
        self.clf = self.export_model()
        logger.info("Model Production Iris Classifier V2 exported and saved")
        self.iris_type = {0: "setosa", 1: "versicolor", 2: "virginica"}
        logger.info("Iris Classifier V2 types set up")

    def train_model(self) -> LogisticRegression:
        return LogisticRegression(
            solver="lbfgs", max_iter=1000, multi_class="multinomial"
        ).fit(self.X, self.y)

    def export_model(self):
        joblib.dump(self.train_model(), "iris_model_prod.pkl")
        logger.info("Model Production Iris Classifier V2 trained")
        return 0

    def load_model(self):
        return joblib.load("iris_model_prod.pkl")

    def classify_iris(self, iris: Iris):
        X = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        model = self.load_model()
        prediction = model.predict_proba([X])
        result = {
            "class": self.iris_type[np.argmax(prediction)],
            "probability": round(max(prediction[0]), 2),
        }
        logger.debug(
            f"The output returned from Production Iris Classifier V2 to the frontend is {result}"
        )
        return result
