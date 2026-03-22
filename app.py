from flask import Flask, render_template, request, jsonify
import joblib
import os
from feature_extractor import extract_features

app = Flask(__name__)

# Load model
MODEL_PATH = "models/phishing_model.pkl"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("[+] Model loaded successfully!")
else:
    print("[!] Model not found! Run train_model.py first.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded. Run train_model.py first."})

    data = request.get_json()
    url  = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Please enter a URL."})

    # Add http if missing
    if not url.startswith("http"):
        url = "http://" + url

    # Extract features and predict
    features    = extract_features(url)
    prediction  = model.predict([features])[0]
    probability = model.predict_proba([features])[0]

    result = {
        "url":           url,
        "prediction":    "Phishing" if prediction == 1 else "Legitimate",
        "confidence":    round(max(probability) * 100, 2),
        "phishing_prob": round(probability[1] * 100, 2),
        "legit_prob":    round(probability[0] * 100, 2),
        "features": {
            "URL Length":        len(url),
            "Has HTTPS":         url.startswith("https"),
            "Has IP Address":    bool(__import__('re').search(
                                 r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url)),
            "Suspicious Words":  any(w in url.lower() for w in
                                 ["login","verify","secure","account",
                                  "password","banking","free","prize"]),
            "Num Subdomains":    len(url.split("/")[2].split(".")) - 2
                                 if "/" in url else 0,
        }
    }

    return jsonify(result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)