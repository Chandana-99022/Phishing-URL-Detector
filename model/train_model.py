import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load feature dataset
data = pd.read_csv("dataset/features_dataset.csv")

print("✅ Feature dataset loaded!")
print("Total records:", len(data))


# Separate features and labels
X = data.drop("label", axis=1)
y = data["label"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)


# Train model
print("\n🤖 Training model...")
model.fit(X_train, y_train)

print("✅ Model training completed!")


# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL RESULTS")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")


# Classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Legitimate", "Phishing"]
))


# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Save model and feature names
model_package = {
    "model": model,
    "features": list(X.columns)
}

joblib.dump(
    model_package,
    "model/phishing_model.pkl"
)


print("\n✅ Model saved successfully!")
print("File: model/phishing_model.pkl")