import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/raw/reviews_with_themes.csv")

# Create plots folder
import os
os.makedirs("plots", exist_ok=True)

# -----------------------------------
# 1. Sentiment Distribution by Bank
# -----------------------------------
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.savefig("plots/sentiment_distribution.png")
plt.close()

# -----------------------------------
# 2. Rating Distribution
# -----------------------------------
plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution per Bank")

plt.savefig("plots/rating_distribution.png")
plt.close()

# -----------------------------------
# 3. Theme Frequency
# -----------------------------------
plt.figure(figsize=(10,5))

theme_counts = df["theme"].value_counts()

sns.barplot(
    x=theme_counts.values,
    y=theme_counts.index
)

plt.title("Theme Frequency")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.savefig("plots/theme_frequency.png")
plt.close()

print("DONE: Visualizations created")