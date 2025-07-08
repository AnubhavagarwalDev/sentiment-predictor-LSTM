# LSTM Sentiment Analysis Streamlit App

This is a simple, lightweight web application for **sentiment analysis** using a pre-trained **LSTM (Long Short-Term Memory)** deep learning model, built with **Keras** and **TensorFlow**, and deployed with **Streamlit**.

The model is trained on the **IMDB Movie Reviews Dataset** — a widely used benchmark for sentiment classification tasks.

---

## 🎯 Features

- ✅ Clean & user-friendly Streamlit web interface
- ✅ Automatic text preprocessing (lowercasing, punctuation removal)
- ✅ Tokenization using saved tokenizer (`tokenizer.pkl`)
- ✅ Sequence padding (maxlen = 200) to match LSTM input requirements
- ✅ Sentiment prediction (Positive / Negative) using pre-trained LSTM model (`lstm_model.keras`)
- ✅ Displays both sentiment label & prediction probability

---

## 🏷️ Dataset Used

- **IMDB Movie Reviews Dataset**  
  Available on [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

