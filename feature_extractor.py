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
        features["num_subdomains"] = max(0, len(domain.split(".")) - 2)
    except:
        features["num_subdomains"] = 0

    # 13. Has suspicious words
    suspicious = ["login", "verify", "update", "secure", "account",
                  "banking", "confirm", "signin", "password", "free",
                  "lucky", "prize", "click", "paypal", "ebay",
                  "urgent", "alert", "suspended", "restore", "claim",
                  "winner", "reward", "bonus", "offer", "deal"]
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

    # 16. Has port number
    features["has_port"] = 1 if re.search(r":\d+", url) else 0

    # 17. Path length
    try:
        parsed  = urllib.parse.urlparse(url)
        features["path_length"] = len(parsed.path)
    except:
        features["path_length"] = 0

    # 18. Number of parameters
    try:
        parsed  = urllib.parse.urlparse(url)
        params  = urllib.parse.parse_qs(parsed.query)
        features["num_params"] = len(params)
    except:
        features["num_params"] = 0

    # 19. Has double slash in path
    features["has_double_slash"] = 1 if "//" in url[7:] else 0

    # 20. TLD is suspicious
    suspicious_tlds = [".tk", ".ml", ".ga", ".cf", ".gq",
                       ".xyz", ".top", ".work", ".click", ".link"]
    features["suspicious_tld"] = 1 if any(
        url.lower().endswith(t) or t + "/" in url.lower()
        for t in suspicious_tlds) else 0

    # 21. Number of % encoded characters
    features["num_percent"] = url.count("%")

    # 22. Has redirect (multiple http in URL)
    features["has_redirect"] = 1 if url.count("http") > 1 else 0

    # 23. Domain has numbers
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc.split(":")[0]
        features["domain_has_numbers"] = 1 if any(
            c.isdigit() for c in domain) else 0
    except:
        features["domain_has_numbers"] = 0

    # 24. URL has brand name in subdomain
    brands = ["paypal", "amazon", "google", "facebook", "microsoft",
              "apple", "netflix", "ebay", "bank", "chase", "wells"]
    try:
        parsed   = urllib.parse.urlparse(url)
        domain   = parsed.netloc.lower()
        parts    = domain.split(".")
        subdomain = ".".join(parts[:-2]) if len(parts) > 2 else ""
        features["brand_in_subdomain"] = 1 if any(
            b in subdomain for b in brands) else 0
    except:
        features["brand_in_subdomain"] = 0

    return list(features.values())