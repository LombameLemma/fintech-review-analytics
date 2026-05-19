import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load sentiment data
df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# Fill missing text (safety)
df["review"] = df["review"].fillna("")

# TF-IDF vectorizer (extract important keywords)
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=30,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df["review"])

keywords = vectorizer.get_feature_names_out()

print("Top Keywords:")
print(keywords)

# Simple rule-based theme assignment
def assign_theme(text):
    text = text.lower()

    if "login" in text or "password" in text:
        return "Login Issues"
    elif "otp" in text or "code" in text:
        return "OTP Problems"
    elif "slow" in text or "transfer" in text:
        return "Transfer Performance"
    elif "crash" in text or "error" in text:
        return "App Stability"
    elif "ui" in text or "design" in text:
        return "UI/UX Feedback"
    elif "feature" in text or "request" in text:
        return "Feature Request"
    else:
        return "Other"

df["theme"] = df["review"].apply(assign_theme)

# Save results
df.to_csv("data/raw/reviews_with_themes.csv", index=False)

print("DONE: Themes extracted")