# Sentiment Analysis on Movie Reviews using LSTM

This project implements a sentiment analysis model to classify IMDb movie reviews as positive or negative. The model is built using TensorFlow and Keras with Long Short-Term Memory (LSTM) layers. The goal of the project is to create a system that can predict the sentiment of a movie review based on its content.

The project includes:
- **Model training** using the IMDb dataset with LSTM for sentiment analysis.
- **Streamlit-based frontend** that allows users to input a movie review and receive a sentiment prediction (positive or negative).

---

## Project Overview

This project leverages a deep learning model (LSTM) to analyze text sentiment. The model is trained on the IMDb movie reviews dataset, which contains 50,000 movie reviews labeled as either positive or negative. The trained model can be used to predict sentiment for new reviews.

The model's architecture consists of an **Embedding layer**, an **LSTM layer**, and a **Dense output layer** with a sigmoid activation function for binary classification.

The frontend of the application is built using **Streamlit**, which provides an interactive web interface for users to input reviews and get instant sentiment predictions.

---

## Features

- **Interactive Web Interface**: Allows users to input movie reviews and get sentiment predictions (positive/negative).
- **Binary Classification**: The model predicts whether a review is positive or negative based on the review content.
- **Real-Time Prediction**: Users can test the model on their own movie reviews.

---

## Model Architecture

The model consists of the following layers:

1. **Embedding Layer**:
   - Converts words into dense vectors of fixed size (128 dimensions).
2. **LSTM Layer**:
   - A Long Short-Term Memory (LSTM) layer with 256 units to capture the sequential dependencies in the text.
3. **Dense Layer**:
   - A fully connected layer with a sigmoid activation function for binary classification.

### Hyperparameters:
- **Max sequence length**: 500
- **Embedding dimensions**: 128
- **LSTM units**: 256
- **Dropout**: 0.2
- **Batch size**: 64
- **Epochs**: 20 (you can increase epochs to improve performance)

---

## Installation

To run this project on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/harsha0014/Sentiment-Analysis-IMDB.git
   cd Sentiment-Analysis-IMDB
