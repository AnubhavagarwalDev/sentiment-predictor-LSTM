import streamlit as st
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import re

def transform_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

@st.cache_resource
def load_tokenizer():
    with open("tokenizer.pkl", "rb") as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

@st.cache_resource
def load_lstm_model():
    model = load_model("sentiment_model.keras")
    return model


st.title("Sentiment Analysis Web App (LSTM)")
user_input = st.text_area("Enter your text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Preprocessing
        preprocessed_text = transform_text(user_input)

        # Tokenization
        tokenizer = load_tokenizer()
        sequence = tokenizer.texts_to_sequences([preprocessed_text])

        # Padding
        padded_sequence =pad_sequences(sequence, maxlen=200)

        #predciton
        model = load_lstm_model()
        prediction = model.predict(padded_sequence)

        # Output Result
        sentiment = "Positive" if prediction[0][0] >= 0.5 else "Negative"
        st.subheader("Sentiment Prediction:")
        st.success(f"**{sentiment}** (Probability: {prediction[0][0]:.2f})")
