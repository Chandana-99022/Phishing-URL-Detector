import pandas as pd
from feature_extraction import extract_features


# Load the prepared dataset
data = pd.read_csv("dataset/combined_dataset.csv")

print("Dataset loaded successfully!")
print("Total URLs:", len(data))


# Extract features from every URL
feature_data = []

for index, url in enumerate(data["URLs"]):

    features = extract_features(url)
    features["label"] = data.loc[index, "label"]

    feature_data.append(features)

    # Show progress
    if (index + 1) % 5000 == 0:
        print(f"Processed {index + 1} URLs...")


# Convert features into a DataFrame
features_df = pd.DataFrame(feature_data)


# Save the feature dataset
features_df.to_csv(
    "dataset/features_dataset.csv",
    index=False
)


print("\n✅ Feature extraction completed!")
print("Total records:", len(features_df))
print("Total features:", len(features_df.columns))

print("\nFeature columns:")
print(features_df.columns.tolist())

print("\nFirst 5 rows:")
print(features_df.head())