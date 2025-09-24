import requests, urllib3, certifi

urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)


def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        resp = requests.get(url, timeout=6, verify=certifi.where())
        resp.raise_for_status()  # akan raise HTTPError jika status != 200
        data = resp.json()
        # Struktur: { "content": "...", "author": "..." , ... }
        return data["content"], data.get("author", "Unknown")
    except requests.exceptions.RequestException as e:
        print("Error saat mengambil quote:", e)
        return None, None


q, a = get_random_quote()
print(f'"{q}" — {a}')
