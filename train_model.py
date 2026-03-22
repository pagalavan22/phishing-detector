import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from feature_extractor import extract_features

print("[*] Generating training dataset...")

# Legitimate URLs
legit_urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.microsoft.com",
    "https://www.amazon.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.apple.com",
    "https://www.netflix.com",
    "https://www.reddit.com",
    "https://www.instagram.com",
    "https://www.dropbox.com",
    "https://www.paypal.com",
    "https://www.ebay.com",
    "https://www.yahoo.com",
    "https://www.bing.com",
    "https://www.adobe.com",
    "https://www.spotify.com",
    "https://www.twitch.tv",
    "https://www.discord.com",
    "https://www.zoom.us",
    "https://www.slack.com",
    "https://www.notion.so",
    "https://www.figma.com",
    "https://www.canva.com",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.khanacademy.org",
    "https://www.medium.com",
    "https://www.quora.com",
    "https://www.pinterest.com",
    "https://www.tumblr.com",
    "https://www.wordpress.com",
    "https://www.shopify.com",
    "https://www.stripe.com",
    "https://www.twilio.com",
    "https://www.heroku.com",
    "https://www.digitalocean.com",
    "https://www.cloudflare.com",
    "https://www.mongodb.com",
    "https://www.postgresql.org",
    "https://www.mysql.com",
    "https://www.oracle.com",
    "https://www.ibm.com",
    "https://www.salesforce.com",
    "https://www.hubspot.com",
    "https://www.zendesk.com",
]

# Phishing URLs
phishing_urls = [
    "http://paypal-verify-account.com/login",
    "http://192.168.1.1/paypal/secure",
    "http://amazon-security-alert.tk/verify",
    "http://login-facebook-secure.ml/account",
    "http://secure-banking-update.com/signin",
    "http://google-account-verify.cf/login",
    "http://microsoft-security-alert.ga/update",
    "http://apple-id-confirm.tk/verify",
    "http://netflix-payment-update.ml/billing",
    "http://ebay-secure-login.cf/confirm",
    "http://paypal.com.secure-login.tk/",
    "http://www.amazon.com-secure.ml/login",
    "http://192.168.0.1/admin/phishing",
    "http://free-prize-winner.com/claim",
    "http://lucky-draw-winner2024.tk/prize",
    "http://bank-account-verify.ml/update",
    "http://credit-card-confirm.cf/billing",
    "http://urgent-security-alert.ga/verify",
    "http://account-suspended-click.tk/restore",
    "http://signin-password-reset.ml/confirm",
    "http://paypal-secure.com.phish.tk/login",
    "http://amazon.account-update.ml/verify",
    "http://facebook.com-login-secure.cf/",
    "http://192.0.2.1/banking/secure/login",
    "http://free-iphone-winner.tk/claim",
    "http://microsoft-update-required.ml/",
    "http://apple-support-verify.cf/id",
    "http://instagram-login-secure.ga/verify",
    "http://twitter-account-update.tk/signin",
    "http://linkedin-verify-account.ml/login",
    "http://dropbox-secure-login.cf/verify",
    "http://spotify-premium-free.tk/activate",
    "http://netflix-free-month.ml/claim",
    "http://amazon-gift-card-winner.cf/prize",
    "http://ebay-account-suspended.ga/restore",
    "http://yahoo-mail-verify.tk/account",
    "http://gmail-account-alert.ml/secure",
    "http://chase-bank-verify.cf/login",
    "http://wells-fargo-secure.ga/signin",
    "http://bank-of-america-update.tk/verify",
    "http://citibank-alert-secure.ml/login",
    "http://hsbc-account-confirm.cf/verify",
    "http://dhl-parcel-update.ga/track",
    "http://fedex-delivery-confirm.tk/verify",
    "http://ups-package-alert.ml/track",
    "http://covid-free-vaccine.cf/register",
    "http://stimulus-check-claim.ga/apply",
    "http://tax-refund-claim.tk/verify",
    "http://irs-refund-secure.ml/claim",
    "http://social-security-verify.cf/update",
]

# Build dataset
urls   = legit_urls + phishing_urls
labels = [0] * len(legit_urls) + [1] * len(phishing_urls)

# Extract features
print("[*] Extracting features...")
X = [extract_features(url) for url in urls]
y = labels

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
print("[*] Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc    = accuracy_score(y_test, y_pred)
print(f"[+] Model Accuracy: {acc*100:.2f}%")
print(classification_report(y_test, y_pred,
      target_names=["Legitimate", "Phishing"]))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/phishing_model.pkl")
print("[+] Model saved to models/phishing_model.pkl")