# 🤖 AI Phishing URL Detector

An AI-powered web application that detects phishing URLs in real-time
using Machine Learning. Trains and compares 5 ML models with 24 URL
features and 300 training samples.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey)
![ML](https://img.shields.io/badge/ML-5%20Models-green)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-brightgreen)
![Features](https://img.shields.io/badge/Features-24-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚀 Features

- **5 ML Models** — Random Forest, SVM, Decision Tree, Logistic Regression, KNN
- **24 URL Features** — Length, entropy, subdomains, suspicious TLDs and more
- **300 Training URLs** — 150 legitimate + 150 phishing URLs
- **Real-time Detection** — Instant prediction with confidence score
- **Model Comparison Dashboard** — Accuracy and CV score charts
- **Confusion Matrix** — Visual performance breakdown
- **URL Analysis** — Detailed feature breakdown for every URL
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
├── app.py                  ← Flask backend + routes
├── feature_extractor.py    ← 24 URL feature extraction
├── train_model.py          ← Train & compare 5 ML models
├── models/
│   ├── phishing_model.pkl  ← Best trained model (Random Forest)
│   ├── scaler.pkl          ← Feature scaler
│   └── results.json        ← Model comparison results
├── templates/
│   ├── index.html          ← Main detection page
│   ├── results.html        ← Model performance dashboard
│   └── about.html          ← How it works page
└── static/
    ├── css/style.css       ← Dark theme styles
    └── js/main.js          ← Frontend prediction logic
```

---

## ⚡ Getting Started
```bash
# Clone the repo
git clone https://github.com/pagalavan22/phishing-detector.git
cd phishing-detector

# Install dependencies
pip install flask scikit-learn pandas numpy joblib beautifulsoup4

# Train all 5 models
python train_model.py

# Run the app
python app.py
```

Then open: **http://127.0.0.1:5000**

---

## 🤖 ML Models Compared

| Model | Accuracy | CV Score |
|-------|----------|----------|
| Random Forest ⭐ | 100.00% | 100.00% |
| Decision Tree | 100.00% | 99.57% |
| SVM | 100.00% | 100.00% |
| Logistic Regression | 100.00% | 100.00% |
| KNN | 100.00% | 99.15% |

**Best Model:** Random Forest with 100 decision trees

---

## 🔍 24 Features Extracted

| # | Feature | Description |
|---|---------|-------------|
| 1 | URL Length | Longer URLs are more suspicious |
| 2 | Number of Dots | More dots indicate subdomains |
| 3 | Number of Hyphens | Hyphens common in phishing |
| 4 | Number of Slashes | Deep paths are suspicious |
| 5 | Has @ Symbol | Used to trick browsers |
| 6 | Has HTTPS | Phishing sites use HTTP |
| 7 | Has IP Address | IPs instead of domains |
| 8 | Domain Length | Short domains are suspicious |
| 9 | Num Subdomains | Too many subdomains = phishing |
| 10 | Suspicious Words | login, verify, secure, prize |
| 11 | Digits in Domain | Numbers in domain name |
| 12 | URL Entropy | High randomness = suspicious |
| 13 | Has Port Number | Unusual ports in URL |
| 14 | Path Length | Very long paths suspicious |
| 15 | Num Parameters | Many params = phishing |
| 16 | Has Double Slash | Redirect trick |
| 17 | Suspicious TLD | .tk .ml .ga .cf .xyz |
| 18 | Percent Encoded | Encoded characters trick |
| 19 | Has Redirect | Multiple http in URL |
| 20 | Domain Has Numbers | Numbers in domain |
| 21 | Brand in Subdomain | paypal.fake.com trick |
| 22 | Num @ Symbols | Used to hide real URL |
| 23 | Num = Symbols | Query parameter count |
| 24 | Num _ Symbols | Underscore in domain |

---

## 🧪 Example Results

| URL | Result | Confidence |
|-----|--------|------------|
| https://www.google.com | ✅ Safe | 80% |
| https://www.github.com | ✅ Safe | 90% |
| https://www.microsoft.com | ✅ Safe | 85% |
| http://paypal-verify-account.com/login | 🚨 Phishing | 99% |
| http://free-prize-winner.tk/claim | 🚨 Phishing | 100% |
| http://192.168.1.1/paypal/secure | 🚨 Phishing | 100% |
| http://amazon-security-alert.tk/verify | 🚨 Phishing | 100% |

---

## 🔧 How It Works
```
URL Input
    │
    ▼
Feature Extraction (24 features)
    │
    ▼
Random Forest Classifier (100 trees)
    │
    ▼
Prediction + Confidence Score + URL Analysis
    │
    ▼
Result displayed on Web UI
```

---

## 📊 Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | / | URL detection page |
| Model Results | /results | ML performance dashboard |
| About | /about | How it works |

---

## 🛡️ Disclaimer

This tool is for **educational purposes only**.
Do not use to test URLs you do not own or have permission to analyse.

---

## 👨‍💻 Author

**Tamil Pagalavan E**
B.E. Computer Science Engineering (Cyber Security)
2024 – 2028 

[![GitHub](https://img.shields.io/badge/GitHub-pagalavan22-181717?logo=github)](https://github.com/pagalavan22)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Tamil%20Pagalavan-0077B5?logo=linkedin)](https://www.linkedin.com/in/tamil-pagalavan-508235328)