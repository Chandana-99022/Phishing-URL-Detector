# 🔐 Phishing URL Detector

## 📌 Project Description

The Phishing URL Detector is a machine-learning-based web application
that analyzes a given URL and predicts whether it is legitimate or
potentially phishing.

The application provides the prediction result, confidence percentage,
risk level, and prediction history through a simple web interface.

## 🎯 Objectives

- Detect potentially phishing URLs
- Classify URLs as legitimate or phishing
- Display prediction confidence
- Display risk level
- Maintain prediction history
- Provide a simple and user-friendly interface

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** to classify URLs.

The model analyzes URL-based features such as:

- URL length
- Hostname length
- Path length
- Number of dots
- Number of hyphens
- Number of slashes
- Number of digits
- Number of letters
- HTTPS usage
- IP address detection
- Subdomain count
- Suspicious words
- URL shortener detection

## 📊 Model Performance

The trained model achieved:

- **Accuracy: 99.23%**
- Training records: **45,056**
- Testing records: **11,264**

The accuracy is based on the project's held-out test dataset.

## ✨ Features

- 🔗 URL input
- 🔍 URL analysis
- 🟢 Legitimate URL detection
- 🔴 Phishing URL detection
- 📊 Confidence percentage
- ⚠️ Risk level
- 🕒 Prediction history
- 🗑️ Clear history option
- 💻 Simple web interface

## 🧪 Example Predictions

## Legitimate URL

```text
https://google.com