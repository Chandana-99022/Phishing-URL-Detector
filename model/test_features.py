from feature_extraction import extract_features


# Test URLs
test_urls = [
    "https://google.com",
    "https://youtube.com",
    "http://secure-login-verify-account.com",
    "http://192.168.1.10/login",
    "https://tinyurl.com/example"
]


for url in test_urls:

    print("\nURL:", url)

    features = extract_features(url)

    for feature, value in features.items():
        print(f"{feature}: {value}")