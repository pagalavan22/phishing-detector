from flask import Flask, render_template, request, jsonify
import joblib
import os
import json
from feature_extractor import extract_features

app = Flask(__name__)

# Load model and scaler
MODEL_PATH   = "models/phishing_model.pkl"
SCALER_PATH  = "models/scaler.pkl"
RESULTS_PATH = "models/results.json"

model   = None
scaler  = None
results = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("[+] Model loaded!")
else:
    print("[!] Model not found! Run train_model.py first.")

if os.path.exists(SCALER_PATH):
    scaler = joblib.load(SCALER_PATH)
    print("[+] Scaler loaded!")

if os.path.exists(RESULTS_PATH):
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    print("[+] Results loaded!")

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

    if not url.startswith("http"):
        url = "http://" + url

    features   = extract_features(url)
    prediction = model.predict([features])[0]
    proba      = model.predict_proba([features])[0]

    result = {
        "url":           url,
        "prediction":    "Phishing" if prediction == 1 else "Legitimate",
        "confidence":    round(max(proba) * 100, 2),
        "phishing_prob": round(proba[1] * 100, 2),
        "legit_prob":    round(proba[0] * 100, 2),
        "features": {
            "URL Length":          len(url),
            "Has HTTPS":           url.startswith("https"),
            "Has IP Address":      bool(__import__("re").search(
                                   r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url)),
            "Suspicious Words":    any(w in url.lower() for w in
                                   ["login","verify","secure","account",
                                    "password","banking","free","prize"]),
            "Suspicious TLD":      any(t in url.lower() for t in
                                   [".tk",".ml",".ga",".cf",".xyz",".top"]),
            "Has Redirect":        url.count("http") > 1,
            "Brand in Subdomain":  any(b in url.lower().split("/")[2].split(".")[:-2]
                                   for b in ["paypal","amazon","google",
                                             "facebook","microsoft","apple"]
                                   if len(url.split("/")) > 2),
            "Num Subdomains":      max(0, len(url.split("/")[2].split(".")) - 2)
                                   if "/" in url else 0,
        }
    }

    return jsonify(result)

@app.route("/results")
def model_results():
    if not results:
        return render_template("results.html", results=None)
    return render_template("results.html", results=results)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)