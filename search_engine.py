import requests
from config import GOOGLE_API_KEY, SEARCH_ENGINE_ID

def google_search(query, num_results=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "num": num_results
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for item in data.get("items", []):
        results.append(f"🔹 {item['title']}\n🔗 {item['link']}\n📄 {item['snippet']}\n")
    
    return "\n".join(results) if results else "⚠️ No results found."
