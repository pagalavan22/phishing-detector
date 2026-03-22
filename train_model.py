import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix)
from sklearn.preprocessing import StandardScaler
import joblib
import os
import json
from feature_extractor import extract_features

print("[*] Generating enhanced training dataset...")

# ── Legitimate URLs (150) ─────────────────────────────────────
legit_urls = [
    "https://www.google.com", "https://www.github.com",
    "https://www.microsoft.com", "https://www.amazon.com",
    "https://www.youtube.com", "https://www.facebook.com",
    "https://www.twitter.com", "https://www.linkedin.com",
    "https://www.stackoverflow.com", "https://www.wikipedia.org",
    "https://www.apple.com", "https://www.netflix.com",
    "https://www.reddit.com", "https://www.instagram.com",
    "https://www.dropbox.com", "https://www.paypal.com",
    "https://www.ebay.com", "https://www.yahoo.com",
    "https://www.bing.com", "https://www.adobe.com",
    "https://www.spotify.com", "https://www.twitch.tv",
    "https://www.discord.com", "https://www.zoom.us",
    "https://www.slack.com", "https://www.notion.so",
    "https://www.figma.com", "https://www.canva.com",
    "https://www.coursera.org", "https://www.udemy.com",
    "https://www.khanacademy.org", "https://www.medium.com",
    "https://www.quora.com", "https://www.pinterest.com",
    "https://www.tumblr.com", "https://www.wordpress.com",
    "https://www.shopify.com", "https://www.stripe.com",
    "https://www.twilio.com", "https://www.heroku.com",
    "https://www.digitalocean.com", "https://www.cloudflare.com",
    "https://www.mongodb.com", "https://www.postgresql.org",
    "https://www.mysql.com", "https://www.oracle.com",
    "https://www.ibm.com", "https://www.salesforce.com",
    "https://www.hubspot.com", "https://www.zendesk.com",
    "https://www.atlassian.com", "https://www.trello.com",
    "https://www.jira.com", "https://www.confluence.com",
    "https://www.bitbucket.org", "https://www.gitlab.com",
    "https://www.docker.com", "https://www.kubernetes.io",
    "https://www.terraform.io", "https://www.ansible.com",
    "https://aws.amazon.com", "https://cloud.google.com",
    "https://azure.microsoft.com", "https://www.linode.com",
    "https://www.vultr.com", "https://www.netlify.com",
    "https://www.vercel.com", "https://www.firebase.google.com",
    "https://www.twilio.com", "https://www.sendgrid.com",
    "https://www.mailchimp.com", "https://www.constant-contact.com",
    "https://www.hootsuite.com", "https://www.buffer.com",
    "https://www.semrush.com", "https://www.ahrefs.com",
    "https://www.moz.com", "https://www.similarweb.com",
    "https://www.hotjar.com", "https://www.mixpanel.com",
    "https://www.segment.com", "https://www.amplitude.com",
    "https://www.datadog.com", "https://www.newrelic.com",
    "https://www.splunk.com", "https://www.elastic.co",
    "https://www.grafana.com", "https://www.prometheus.io",
    "https://www.jenkins.io", "https://www.travis-ci.com",
    "https://www.circleci.com", "https://www.github.com/actions",
    "https://www.sonarqube.org", "https://www.snyk.io",
    "https://www.owasp.org", "https://www.sans.org",
    "https://www.nist.gov", "https://www.cisa.gov",
    "https://www.cert.org", "https://nvd.nist.gov",
    "https://www.virustotal.com", "https://www.shodan.io",
    "https://www.metasploit.com", "https://www.kali.org",
    "https://www.wireshark.org", "https://nmap.org",
    "https://www.python.org", "https://www.javascript.com",
    "https://www.typescriptlang.org", "https://reactjs.org",
    "https://vuejs.org", "https://angular.io",
    "https://nodejs.org", "https://expressjs.com",
    "https://flask.palletsprojects.com", "https://www.djangoproject.com",
    "https://fastapi.tiangolo.com", "https://spring.io",
    "https://www.rust-lang.org", "https://golang.org",
    "https://www.scala-lang.org", "https://www.kotlin.org",
    "https://www.swift.org", "https://www.dartlang.org",
    "https://flutter.dev", "https://reactnative.dev",
    "https://www.tensorflow.org", "https://pytorch.org",
    "https://scikit-learn.org", "https://pandas.pydata.org",
    "https://numpy.org", "https://matplotlib.org",
    "https://seaborn.pydata.org", "https://plotly.com",
    "https://www.kaggle.com", "https://huggingface.co",
    "https://openai.com", "https://www.anthropic.com",
    "https://www.deepmind.com", "https://research.google.com",
    "https://ai.facebook.com", "https://www.nvidia.com",
    "https://www.intel.com", "https://www.amd.com",
    "https://www.qualcomm.com", "https://www.arm.com",
    "https://www.samsung.com", "https://www.sony.com",
    "https://www.lg.com", "https://www.dell.com",
    "https://www.hp.com", "https://www.lenovo.com",
    "https://www.asus.com", "https://www.acer.com",
]

# ── Phishing URLs (150) ───────────────────────────────────────
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
    "http://10.0.0.1/admin/login",
    "http://172.16.0.1/bank/secure",
    "http://account-locked-verify.xyz/unlock",
    "http://your-account-suspended.top/restore",
    "http://click-here-free-gift.work/claim",
    "http://win-iphone14-now.link/register",
    "http://paypal.security-update.xyz/verify",
    "http://amazon.login-confirm.top/account",
    "http://google.account-recover.work/signin",
    "http://facebook.login-secure.click/verify",
    "http://secure.paypal.com.phishing.tk/",
    "http://update.microsoft.com.malware.ml/",
    "http://signin.google.com.fake.cf/login",
    "http://login.amazon.com.spoof.ga/verify",
    "http://account.apple.com.phish.tk/id",
    "http://verify.bank.com.fake.ml/login",
    "http://confirm.ebay.com.spoof.cf/account",
    "http://secure.netflix.com.phish.ga/",
    "http://update.dropbox.com.fake.tk/login",
    "http://signin.instagram.com.spoof.ml/",
    "http://free-bitcoin-generator.xyz/claim",
    "http://earn-money-online-fast.top/join",
    "http://work-from-home-$$$.click/apply",
    "http://get-rich-quick-scheme.link/invest",
    "http://lottery-winner-2024.xyz/claim",
    "http://prize-notification-official.top/",
    "http://congratulations-you-won.work/",
    "http://exclusive-offer-members.click/",
    "http://limited-time-deal-today.link/buy",
    "http://special-discount-coupon.xyz/get",
    "http://account-password-expired.tk/reset",
    "http://email-verify-required.ml/confirm",
    "http://profile-update-needed.cf/update",
    "http://billing-failed-retry.ga/payment",
    "http://subscription-expired-renew.tk/",
    "http://security-breach-detected.ml/fix",
    "http://virus-found-clean-now.cf/scan",
    "http://your-pc-infected-fix.ga/remove",
    "http://malware-detected-urgent.tk/clean",
    "http://system-error-fix-now.ml/repair",
    "http://193.128.0.1/phishing/login",
    "http://10.10.10.1/bank/verify",
    "http://172.31.0.1/paypal/signin",
    "http://192.168.100.1/admin/secure",
    "http://203.0.113.1/account/verify",
    "http://198.51.100.1/login/confirm",
    "http://customer-service-help.xyz/verify",
    "http://support-team-online.top/help",
    "http://helpdesk-urgent-matter.work/fix",
    "http://technical-support-needed.click/",
    "http://your-refund-ready.link/claim",
    "http://refund-process-pending.xyz/verify",
    "http://cashback-offer-today.top/claim",
    "http://reward-points-expire.work/redeem",
    "http://bonus-cash-available.click/get",
    "http://gift-card-winner.link/claim",
    "http://survey-complete-reward.xyz/",
    "http://feedback-bonus-offer.top/submit",
    "http://participation-prize.work/collect",
    "http://exclusive-member-reward.click/",
    "http://identity-verify-secure.tk/id",
    "http://document-verification.ml/upload",
    "http://kyc-update-required.cf/submit",
    "http://aadhar-verify-online.ga/confirm",
    "http://pan-card-update.tk/verify",
    "http://bank-kyc-deadline.ml/update",
    "http://wallet-verify-account.cf/confirm",
    "http://upi-account-suspended.ga/restore",
    "http://phonepe-alert-secure.tk/verify",
    "http://gpay-login-confirm.ml/signin",
    "http://paytm-verify-secure.cf/account",
    "http://bhim-update-required.ga/verify",
    "http://sbi-alert-login.tk/secure",
    "http://hdfc-account-verify.ml/login",
    "http://icici-secure-signin.cf/verify",
    "http://axis-bank-alert.ga/confirm",
    "http://kotak-login-secure.tk/verify",
    "http://rbl-bank-update.ml/signin",
    "http://yes-bank-verify.cf/account",
    "http://indusind-secure.ga/login",
    "http://bandhan-bank-alert.tk/verify",
    "http://irctc-ticket-free.ml/book",
    "http://railway-refund-claim.cf/verify",
    "http://flipkart-order-verify.ga/confirm",
    "http://myntra-offer-winner.tk/claim",
    "http://zomato-free-food.ml/offer",
    "http://swiggy-bonus-cash.cf/redeem",
    "http://ola-ride-free.ga/coupon",
    "http://uber-bonus-trip.tk/claim",
    "http://amazon-india-offer.ml/verify",
]

# Build dataset
urls   = legit_urls + phishing_urls
labels = [0] * len(legit_urls) + [1] * len(phishing_urls)

# Extract features
print("[*] Extracting 24 features from each URL...")
X = [extract_features(url) for url in urls]
y = labels

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale for SVM and Logistic Regression
scaler  = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# ── Train 5 models ────────────────────────────────────────────
models = {
    "Random Forest":     RandomForestClassifier(n_estimators=100, random_state=42),
    "Decision Tree":     DecisionTreeClassifier(random_state=42),
    "SVM":               SVC(probability=True, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "KNN":               KNeighborsClassifier(n_neighbors=5),
}

results = {}
best_model     = None
best_accuracy  = 0
best_model_name = ""

print("\n[*] Training and comparing 5 ML models...\n")
print(f"{'Model':<25} {'Accuracy':>10} {'CV Score':>10}")
print("-" * 48)

for name, model in models.items():
    # Use scaled data for SVM and LR
    if name in ["SVM", "Logistic Regression"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        cv_scores = cross_val_score(model, X_train_scaled,
                                    y_train, cv=5)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)

    acc = accuracy_score(y_test, y_pred)
    cv  = cv_scores.mean()

    print(f"{name:<25} {acc*100:>9.2f}% {cv*100:>9.2f}%")

    results[name] = {
        "accuracy":  round(acc * 100, 2),
        "cv_score":  round(cv * 100, 2),
        "confusion": confusion_matrix(y_test, y_pred).tolist()
    }

    if acc > best_accuracy:
        best_accuracy   = acc
        best_model      = model
        best_model_name = name

print(f"\n[+] Best model: {best_model_name} ({best_accuracy*100:.2f}%)")

# Save best model + scaler + results
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/phishing_model.pkl")
joblib.dump(scaler,     "models/scaler.pkl")

with open("models/results.json", "w") as f:
    json.dump({
        "best_model":    best_model_name,
        "best_accuracy": round(best_accuracy * 100, 2),
        "models":        results
    }, f, indent=4)

print("[+] Model saved:   models/phishing_model.pkl")
print("[+] Scaler saved:  models/scaler.pkl")
print("[+] Results saved: models/results.json")
print("\n[*] Training complete!")