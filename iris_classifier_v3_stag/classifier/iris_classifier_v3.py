import joblib
import logging
import sys

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from models.models import Iris

sys.path.append("..")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("stag_iris_classifier_v3.log")
file_handler.setFormatter(formatter)

# THIS IS THE NEW CHANGE TO STREAM LOGS
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        logger.info("Data Staging Iris Classifier V3 loaded")
        self.clf = self.export_model()
        logger.info("Model Staging Iris Classifier V3 exported and saved")
        self.iris_type = ["setosa", "versicolor", "virginica"]
        logger.info("Iris Classifier V3 types set up")

    def train_model(self) -> RandomForestClassifier:
        return RandomForestClassifier(n_estimators=100).fit(self.X, self.y)

    def export_model(self):
        joblib.dump(self.train_model(), "iris_model_v3_stag.pkl")
        logger.info("Model Staging Iris Classifier V3 trained")
        return 0

    def load_model(self):
        return joblib.load("iris_model_v3_stag.pkl")

    def classify_iris(self, iris: Iris):
        X = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        model = self.load_model()
        species_idx = model.predict([X])[0]
        class_iris = self.iris_type[species_idx]
        result = {"class": class_iris}
        logger.debug(
            f"The output returned from Staging Iris Classifier V3 to the frontend is {result}"
        )
        return result
