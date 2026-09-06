# DSD Resort AI Engine

This repository contains the AI/Machine Learning backend for the DSD Resort Admin project, built with FastAPI. It provides predictive analytics and natural language processing capabilities.

## Features

- **Guest Demand Forecasting:** Predicts the number of guests/demand based on historical data and environmental factors like weather.
- **Sentiment Analysis:** Analyzes restaurant reviews to determine whether the sentiment is positive or negative along with a confidence score.

## Dataset Details

The models are trained using the following datasets located in the `data/` directory:

- `Restaurant_Reviews.tsv`: The sentiment analysis model uses the [Restaurant Reviews dataset](https://www.kaggle.com/code/apekshakom/sentiment-analysis-of-restaurant-reviews) (referenced from Kaggle) to classify text as Positive (1) or Negative (0).
- `dsd_raw_sales_data.csv` & `dsd_engineered_data.csv`: These contain raw and feature-engineered sales data, used for forecasting restaurant guest demand.

## Tech Stack

- **FastAPI & Uvicorn:** High-performance web framework and server for building and running the API.
- **Scikit-Learn & XGBoost:** Used for training the forecasting and NLP models.
- **NLTK:** Natural Language Toolkit used for text preprocessing (stemming, stopword removal).
- **Pandas & NumPy:** For data manipulation, feature engineering, and preprocessing.

## Installation & Running Locally

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI application:
   ```bash
   python main.py
   ```
   Or using Uvicorn directly:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

4. The API will be available at `http://127.0.0.1:8000`. You can test the endpoints at `http://127.0.0.1:8000/docs` (Swagger UI).

## Directory Structure

- `data/`: Contains the datasets (`.csv`, `.tsv`) used for training models.
- `engines/`: Contains the core ML inference logic (`demand_forecaster.py` and `nlp_engine.py`).
- `routers/`: Contains the FastAPI routers mapping API endpoints to the engines.
- `static/model/`: Stores the trained serialized model files (`.pkl` and `.pickle`).
- `notebooks/`: Jupyter notebooks used for data exploration, model training, and evaluation.