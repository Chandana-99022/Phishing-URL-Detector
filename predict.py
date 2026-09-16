import joblib
from model.feature_extraction import extract_features


# Load the trained model
model_package = joblib.load("model/phishing_model.pkl")

model = model_package["model"]
feature_names = model_package["features"]


def predict_url(url):
    # Extract features from the URL
    features = extract_features(url)

    # Convert features to the same order used during training
    feature_values = [features[name] for name in feature_names]

    # Make prediction
    prediction = model.predict([feature_values])[0]

    # Get probability
    probabilities = model.predict_proba([feature_values])[0]
    confidence = max(probabilities) * 100

    if prediction == 1:
        result = "🔴 PHISHING URL"
    else:
        result = "🟢 LEGITIMATE URL"

    return result, confidence


# Main program
print("====================================")
print("      PHISHING URL DETECTOR")
print("====================================")

while True:

    url = input("\nEnter a URL (or type 'exit' to quit): ")

    if url.lower() == "exit":
        print("Exiting...")
        break

    result, confidence = predict_url(url)

    print("\nResult:", result)
    print(f"Confidence: {confidence:.2f}%")