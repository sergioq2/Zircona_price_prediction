# Zircona Price Prediction App

This repository contains an application that predicts the price of zircona using machine learning. The application is built with FastAPI and utilizes microservices for prediction and preprocessing. It also includes Jupyter notebooks for exploratory data analysis (EDA) and modeling.

## Notebooks

The `Notebooks` folder contains Jupyter notebook files:

- `EDA.ipynb`: Exploratory Data Analysis of the zircona dataset.
- `Modeling.ipynb`: Machine learning modeling for price prediction.

## Deploy

The `Deploy` folder includes the FastAPI application and deployment files:

- `APP`: The FastAPI application that provides an interface for price prediction.
- `microservices`: Microservices for prediction and preprocessing of data and features.
- `Dockerfile`: Dockerfile to containerize the FastAPI application.

### Usage Instructions

To use the Zircona Price Prediction App, follow these steps:

1. Pull the Docker image:
docker pull docker.io/sergioq2/diamond-app

2. Run the Docker container:
docker run -p 80:80 docker.io/sergioq2/diamond-app


### Machine Learning Model Performance

The selected machine learning model is Random Forest with the following performance metrics:

- R2 Adjust (Train): 99%
- R2 Adjust (Test): 98%
- RMSE (Train): 362.85
- RMSE (Test): 550.9

## MLFlow

MLFlow was used to track experiments for each machine learning model. All experiments are stored in the `mlruns` folder.

---

Feel free to explore the notebooks, experiment with the Zircona Price Prediction App, and review the machine learning model's performance metrics.

For any questions or issues, please feel free to open an issue or contact the repository owner.

Happy exploring and predicting!
