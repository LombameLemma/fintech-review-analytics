import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/reviews_raw.csv")

print("Original shape:", df.shape)

# 1. Remove duplicates
df = df.drop_duplicates(subset=["review", "rating", "date", "bank"])

# 2. Drop missing values
df = df.dropna(subset=["review", "rating"])

# 3. Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# 4. Final structure check
print("Cleaned shape:", df.shape)

# 5. Save cleaned dataset
df.to_csv("data/raw/reviews_clean.csv", index=False)

print("DONE: Clean dataset saved")