
# Serving Iris Classifier with FastAPI + Docker Compose
## fastapi-docker-iris

This is an example of how to serve a machine learning model with a frontend connected to a server that makes the predictions. This is performed by using Docker, Docker Compose, FastApi, Logging, Unit test with Pytest, and more.


## Data

The Iris dataset is a simple, yet popular dataset consisting of 150 observations. Each observation captures the sepal length, sepal width, petal length, petal width of an iris (all in cm) and the corresponding iris subclass (one of *setosa, versicolor, virginica*).

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

# Setup
## Install Docker and Docker Compose
* [Windows](https://docs.docker.com/desktop/windows/install/)
* [Linux](https://docs.docker.com/compose/install/)
* [Mac](https://docs.docker.com/desktop/mac/install/)

## Ensure Docker and Docker Compose are available
* Run this command to check Docker
```
$ docker --version
Docker version 20.10.12, build e91ed57
```
* Run this command to check Docker Compose
```
$ docker-compose version
docker-compose version 1.29.2, build 5becea4c
```
## Clone the project
* Just open your terminal, go or create a directory, and run the following command:
```
$ git clone https://github.com/carloslme/fastapi-docker-iris.git
```
* Change the branch
```
$ git checkout dev
```


# Usage
## Create the network
First create the network AIService by running this command:
```
$ docker network create AIservice
```

## Run Docker Compose
* Be sure you are un the directory where the docker-compose.yml file is located
* Run next command to start the Server and Frontend APIs
```
$ docker-compose up --build
```
You will see something like this:
```
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
Starting iris-api-dev_iris_classifier_v1_stag_1 ... done
Starting iris-api-dev_iris_classifier_v2_prod_1 ... done
Starting iris-api-dev_iris_classifier_v1_prod_1 ... done
Starting iris-api-dev_iris_classifier_v3_stag_1 ... done
Starting iris-api-dev_iris_classifier_v2_stag_1 ... done
Starting iris-api-dev_frontend_1                ... done
Attaching to iris-api-dev_iris_classifier_v1_stag_1, iris-api-dev_iris_classifier_v2_stag_1, iris-api-dev_iris_classifier_v3_stag_1, iris-api-dev_iris_classifier_v1_prod_1, iris-api-dev_iris_classifier_v2_prod_1, iris-api-dev_frontend_1
.
.
.
```
## Open and check APIs
* To open the Frontend, go to the address http://0.0.0.0:3000, you will see the message "Front-end is all ready to go!"


## Test request
The input is a JSON with the following fields:

* sepal_length
* sepal_width
* petal_length
* petal_width

Corresponding values are the measurements in cm.


### CURL request

```
curl -X 'POST' \
  'http://localhost:3000/prod/v2/classify_iris' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"sepal_length": 5, "sepal_width": 2, "petal_length": 3, "petal_width": 4}'
```
### FastAPI UI request
* Go to the http://localhost:3000/docs, and in the POST request body `/prod/v2/classify_iris` copy this:
```
{"sepal_length": 5, "sepal_width": 2, "petal_length": 3, "petal_width": 4}
```
You will get a response body like this:
```
{
  "response": "{\"class\":\"virginica\",\"probability\":0.91}"
}
```


# Check logs
## Extract logs
* Open a new terminal, and change the working directory where the `docker-compose.yml` is located.
* Run the following code to identify the `CONTAINER ID` of the Server container.
```
docker ps -a
```
You will get something like this
```
CONTAINER ID   IMAGE                   COMMAND                  CREATED        STATUS        PORTS                    NAMES
bd1d9305d2d0   iris-api-dev_frontend   "uvicorn main:app --…"   12 hours ago   Up 12 hours   0.0.0.0:3000->3000/tcp   iris-api-dev_frontend_1
568ee652e7e1   iris-api-dev_server     "uvicorn main:app --…"   12 hours ago   Up 12 hours   0.0.0.0:8000->8000/tcp   iris-api-dev_server_1
```
* To extract the logs, you can copy them to your local machine by running this command.
```
docker cp 568ee652e7e1:/app/server.log .
```
You can check the logs.log file in your local directory.