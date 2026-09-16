import pandas as pd

# Load datasets
phishing = pd.read_csv("dataset/urlsfish.csv")
legitimate = pd.read_csv("dataset/urlsgood.csv")

# Add labels
phishing["label"] = 1
legitimate["label"] = 0

# Combine both datasets
data = pd.concat([phishing, legitimate], ignore_index=True)

# Keep only required columns
data = data[["URLs", "label"]]

# Remove duplicate URLs
data = data.drop_duplicates(subset="URLs")

# Remove empty URLs
data = data.dropna(subset=["URLs"])

# Shuffle the dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save prepared dataset
data.to_csv("dataset/combined_dataset.csv", index=False)

# Display information
print("✅ Dataset prepared successfully!")
print("Total URLs:", len(data))
print("\nLabel distribution:")
print(data["label"].value_counts())

print("\nFirst 5 records:")
print(data.head())