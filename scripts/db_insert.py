import pandas as pd
import psycopg2

# Load final dataset
df = pd.read_csv("data/raw/reviews_with_themes.csv")

conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert banks (simple static insert)
banks = {
    "CBE": "Commercial Bank App",
    "BOA": "Bank of Abyssinia App",
    "Dashen": "Dashen Bank App"
}

bank_ids = {}

for bank, app in banks.items():
    cur.execute(
        "INSERT INTO banks (bank_name, app_name) VALUES (%s, %s) RETURNING bank_id",
        (bank, app)
    )
    bank_ids[bank] = cur.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (
            bank_id, review_text, rating, review_date,
            sentiment_label, sentiment_score, theme, source
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
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
cur.close()
conn.close()

print("DONE: Data inserted into PostgreSQL")