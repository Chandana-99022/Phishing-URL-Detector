import re
from urllib.parse import urlparse


def extract_features(url):
    """Extract security-related features from a URL."""

    url = str(url).strip()

    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url_for_parse = "http://" + url
    else:
        url_for_parse = url

    parsed = urlparse(url_for_parse)

    hostname = parsed.netloc
    path = parsed.path
    query = parsed.query

    features = {}

    # Basic URL features
    features["url_length"] = len(url)
    features["hostname_length"] = len(hostname)
    features["path_length"] = len(path)
    features["query_length"] = len(query)

    # Character counts
    features["dot_count"] = url.count(".")
    features["hyphen_count"] = url.count("-")
    features["underscore_count"] = url.count("_")
    features["slash_count"] = url.count("/")
    features["question_count"] = url.count("?")
    features["equal_count"] = url.count("=")
    features["at_count"] = url.count("@")
    features["ampersand_count"] = url.count("&")
    features["percent_count"] = url.count("%")

    # Digits and letters
    features["digit_count"] = sum(char.isdigit() for char in url)
    features["letter_count"] = sum(char.isalpha() for char in url)

    # HTTPS
    features["has_https"] = int(url.lower().startswith("https://"))

    # IP address detection
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    clean_hostname = hostname.split(":")[0]

    features["has_ip"] = int(
        re.match(ip_pattern, clean_hostname) is not None
    )

    # Subdomain count
    if clean_hostname:
        features["subdomain_count"] = max(
            0,
            len(clean_hostname.split(".")) - 2
        )
    else:
        features["subdomain_count"] = 0

    # Suspicious words
    suspicious_words = [
        "login",
        "signin",
        "verify",
        "verification",
        "secure",
        "account",
        "update",
        "confirm",
        "bank",
        "password",
        "payment",
        "paypal",
        "free",
        "bonus",
        "winner",
        "claim",
        "recover"
    ]

    url_lower = url.lower()

    features["suspicious_word_count"] = sum(
        word in url_lower for word in suspicious_words
    )

    # URL shortener detection
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "is.gd",
        "ow.ly",
        "buff.ly",
        "cutt.ly"
    ]

    features["is_shortened"] = int(
        any(
            shortener in clean_hostname.lower()
            for shortener in shorteners
        )
    )

    return features