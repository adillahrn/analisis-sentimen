from google_play_scraper import reviews
import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def scrape_gojek():
    result, _ = reviews(
        'com.gojek.app',
        lang='id',
        country='id',
        count=10000
    )

    df = pd.DataFrame(result)
    df = df[['content', 'score']]

    df['clean'] = df['content'].apply(clean_text)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df.to_csv('gojek_raw.csv', index=False)

    print("Done:", df.shape)

if __name__ == "__main__":
    scrape_gojek()
