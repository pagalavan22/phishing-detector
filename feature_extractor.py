import re
import urllib.parse
import math

def extract_features(url):
    features = {}

    # 1. URL length
    features["url_length"] = len(url)

    # 2. Number of dots
    features["num_dots"] = url.count(".")

    # 3. Number of hyphens
    features["num_hyphens"] = url.count("-")

    # 4. Number of slashes
    features["num_slashes"] = url.count("/")

    # 5. Number of @ symbols
    features["num_at"] = url.count("@")

    # 6. Number of ? symbols
    features["num_question"] = url.count("?")

    # 7. Number of = symbols
    features["num_equals"] = url.count("=")

    # 8. Number of underscores
    features["num_underscore"] = url.count("_")

    # 9. Has HTTPS
    features["has_https"] = 1 if url.startswith("https") else 0

    # 10. Has IP address
    ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    features["has_ip"] = 1 if ip_pattern.search(url) else 0

    # 11. Domain length
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        features["domain_length"] = len(domain)
    except:
        features["domain_length"] = 0

    # 12. Number of subdomains
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        features["num_subdomains"] = len(domain.split(".")) - 2
    except:
        features["num_subdomains"] = 0

    # 13. Has suspicious words
    suspicious = ["login", "verify", "update", "secure", "account",
                  "banking", "confirm", "signin", "password", "free",
                  "lucky", "prize", "click", "paypal", "ebay"]
    url_lower = url.lower()
    features["has_suspicious_words"] = 1 if any(
        w in url_lower for w in suspicious) else 0

    # 14. Number of digits in domain
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        features["digits_in_domain"] = sum(c.isdigit() for c in domain)
    except:
        features["digits_in_domain"] = 0

    # 15. URL entropy
    if len(url) > 0:
        freq = {}
        for c in url:
            freq[c] = freq.get(c, 0) + 1
        entropy = -sum((f/len(url)) * math.log2(f/len(url))
                       for f in freq.values())
        features["url_entropy"] = round(entropy, 4)
    else:
        features["url_entropy"] = 0

    return list(features.values())