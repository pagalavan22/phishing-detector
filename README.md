# 🔍 AI Phishing URL Detector

An AI-powered web application that detects phishing URLs in real-time
using Machine Learning. Built with Python Flask and Random Forest classifier.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey)
![ML](https://img.shields.io/badge/ML-Random%20Forest-green)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚀 Features

- **AI Detection** — Random Forest classifier with 100 decision trees
- **Real-time Analysis** — Instant prediction on any URL
- **Confidence Score** — Shows how confident the model is
- **URL Analysis** — Breaks down 15 features of the URL
- **Dark Theme UI** — Professional dark-themed web interface
- **Example URLs** — Click-to-test safe and phishing examples

---

## 📋 Requirements
```
Python 3.x
pip install flask scikit-learn pandas numpy joblib beautifulsoup4
```

---

## 📁 Project Structure
```
phishing-detector/
├── app.py                  ← Flask backend
├── feature_extractor.py    ← URL feature extraction (15 features)
├── train_model.py          ← Model training script
├── models/
│   └── phishing_model.pkl  ← Trained Random Forest model
├── templates/
│   ├── index.html          ← Main detection page
│   └── about.html          ← How it works page
└── static/
    ├── css/style.css       ← Dark theme styles
    └── js/main.js          ← Frontend logic
```

---

## ⚡ Getting Started
```bash
# Clone the repo
git clone https://github.com/pagalavan22/phishing-detector.git
cd phishing-detector

# Install dependencies
pip install flask scikit-learn pandas numpy joblib beautifulsoup4

# Train the model
python train_model.py

# Run the app
python app.py
```

Then open: **http://127.0.0.1:5000**

---

## 🤖 How The ML Model Works
```
URL Input
    │
    ▼
Feature Extraction (15 features)
    │
    ├── URL Length
    ├── Number of dots, hyphens, slashes
    ├── Has HTTPS
    ├── Has IP Address
    ├── Suspicious keywords (login, verify, secure...)
    ├── Domain length
    ├── Number of subdomains
    └── URL Entropy (randomness score)
    │
    ▼
Random Forest Classifier (100 trees)
    │
    ▼
Prediction + Confidence Score
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| Precision | 1.00 |
| Recall | 1.00 |
| F1 Score | 1.00 |

---

## 🧪 Example Results

| URL | Result | Confidence |
|-----|--------|------------|
| https://www.google.com | ✅ Safe | 80% |
| https://www.github.com | ✅ Safe | 90% |
| http://paypal-verify-account.com/login | 🚨 Phishing | 100% |
| http://free-prize-winner.tk/claim | 🚨 Phishing | 100% |

---

## 🛡️ Disclaimer

This tool is for **educational purposes only**.
Do not use to test URLs you do not own or have permission to test.

---

## 👨‍💻 Author

**Tamil Pagalavan E**
B.E. Computer Science Engineering (Cyber Security)
2024 – 2028 | Aspiring Security Engineer

[![GitHub](https://img.shields.io/badge/GitHub-pagalavan22-181717?logo=github)](https://github.com/pagalavan22)