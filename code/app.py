import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the pre-trained model
model = tf.keras.models.load_model('imdb_rnn_model.h5')

# Function to predict sentiment
def predict_sentiment(text):
    # Tokenize and pad the text
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
    tokenizer.fit_on_texts([text])
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=256, padding='post')

    # Predict the sentiment
    prediction = model.predict(padded_sequence)
    if prediction >= 0.5:
        return 'Positive'
    else:
        return 'Negative'

# Streamlit user interface
st.title('IMDb Movie Review Sentiment Analysis')

review_text = st.text_area("Enter movie review:")

if st.button('Predict Sentiment'):
    if review_text:
        sentiment = predict_sentiment(review_text)
        st.write(f"Sentiment: {sentiment}")
    else:
        st.write("Please enter a review to analyze.")
