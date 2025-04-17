# scraper.py
import requests
from dotenv import load_dotenv
import os 
load_dotenv()
news_api_key = os.getenv("news_api")
def fetch_news_articles(query, api_key=news_api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=3&apiKey={api_key}"
    response = requests.get(url)
    print(response.json()["articles"])
    return response.json()["articles"]
