import pandas as pd
from transformers import pipeline

# Load data
df = pd.read_csv("data/raw/reviews_clean.csv")

# Load sentiment model (DistilBERT)
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

labels = []
scores = []

for text in df["review"]:
    result = sentiment_model(str(text))[0]
    labels.append(result["label"])
    scores.append(result["score"])

df["sentiment_label"] = labels
df["sentiment_score"] = scores

# Save result
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print("DONE: Sentiment analysis completed")