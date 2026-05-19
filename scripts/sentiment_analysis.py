import pandas as pd

df = pd.read_csv("data/raw/reviews_clean.csv")

# Simple rule-based sentiment (safe + fast)
def get_sentiment(text):
    text = str(text).lower()

    positive_words = ["good", "great", "excellent", "fast", "love", "easy", "nice"]
    negative_words = ["bad", "slow", "crash", "error", "fail", "problem", "issue"]

    score = 0

    for w in positive_words:
        if w in text:
            score += 1

    for w in negative_words:
        if w in text:
            score -= 1

    if score > 0:
        return "POSITIVE", 0.8
    elif score < 0:
        return "NEGATIVE", 0.8
    else:
        return "NEUTRAL", 0.5

labels = []
scores = []

for r in df["review"]:
    label, score = get_sentiment(r)
    labels.append(label)
    scores.append(score)

df["sentiment_label"] = labels
df["sentiment_score"] = scores

df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print("DONE: Sentiment completed (no torch version)")