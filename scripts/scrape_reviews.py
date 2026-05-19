from google_play_scraper import reviews, Sort
import pandas as pd

banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_data = []

for bank_name, app_id in banks.items():
    print(f"Scraping {bank_name}...")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        all_data.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        })

df = pd.DataFrame(all_data)

print(df.head())

df.to_csv("data/raw/reviews_raw.csv", index=False)

print("DONE: Data saved")