import pandas as pd
import sqlite3

# Load final processed dataset
df = pd.read_csv("data/raw/reviews_with_themes.csv")

# Connect to SQLite database
conn = sqlite3.connect("bank_reviews.db")

cur = conn.cursor()

# Create banks table
cur.execute("""
CREATE TABLE IF NOT EXISTS banks (
    bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bank_name TEXT,
    app_name TEXT
)
""")

# Create reviews table
cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bank_id INTEGER,
    review_text TEXT,
    rating INTEGER,
    review_date TEXT,
    sentiment_label TEXT,
    sentiment_score REAL,
    theme TEXT,
    source TEXT,
    FOREIGN KEY(bank_id) REFERENCES banks(bank_id)
)
""")

# Insert banks
banks = {
    "CBE": "Commercial Bank App",
    "BOA": "Bank of Abyssinia App",
    "Dashen": "Dashen Bank App"
}

bank_ids = {}

for bank, app in banks.items():
    cur.execute(
        "INSERT INTO banks (bank_name, app_name) VALUES (?, ?)",
        (bank, app)
    )
    bank_ids[bank] = cur.lastrowid

# Insert reviews
for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO reviews (
        bank_id, review_text, rating, review_date,
        sentiment_label, sentiment_score, theme, source
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        bank_ids[row["bank"]],
        row["review"],
        row["rating"],
        row["date"],
        row["sentiment_label"],
        row["sentiment_score"],
        row["theme"],
        row["source"]
    ))

conn.commit()

# Verification queries
print("\nTotal reviews:")
for row in cur.execute("SELECT COUNT(*) FROM reviews"):
    print(row)

print("\nReviews per bank:")
for row in cur.execute("""
SELECT banks.bank_name, COUNT(*)
FROM reviews
JOIN banks ON reviews.bank_id = banks.bank_id
GROUP BY banks.bank_name
"""):
    print(row)

conn.close()

print("\nDONE: SQLite database created successfully")