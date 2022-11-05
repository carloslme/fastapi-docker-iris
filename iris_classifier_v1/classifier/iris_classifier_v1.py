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

file_handler = logging.FileHandler("iris_classifier_v1.log")
file_handler.setFormatter(formatter)

# THIS IS THE NEW CHANGE TO STREAM LOGS
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        logger.info("Data Iris Classifier V1 loaded")
        self.clf = self.train_model()
        logger.info("Model Iris Classifier V1 trained")
        self.iris_type = {0: "setosa", 1: "versicolor", 2: "virginica"}
        logger.info("Iris Classifier V1 types set up")

    def train_model(self) -> LogisticRegression:
        return LogisticRegression(
            solver="lbfgs", max_iter=1000, multi_class="multinomial"
        ).fit(self.X, self.y)

    def classify_iris(self, iris: Iris):
        X = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        prediction = self.clf.predict_proba([X])
        result = {
            "class": self.iris_type[np.argmax(prediction)],
            "probability": round(max(prediction[0]), 2),
        }
        logger.debug(f"The output returned to the frontend is {result}")
        return result
