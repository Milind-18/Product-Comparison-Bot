import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SERPER_API_KEY")

query = "Samsung Galaxy S25 5G vs OnePlus 13 5G"
url = "https://google.serper.dev/search"
headers = {
    "X-API-KEY": api_key,
    "Content-Type": "application/json"
}
payload = {
    "q": query
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

for idx, result in enumerate(data.get("organic", []), 1):
    print(f"{idx}. {result['title']}")
    print(f"   Link: {result['link']}")
    print(f"   Snippet: {result['snippet']}")
    print()
