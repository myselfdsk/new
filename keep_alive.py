import requests

URL = "https://new-ugt0.onrender.com/info?uid=70393167"

try:
    response = requests.get(URL, timeout=30)

    print("=" * 50)
    print("Render Keep Alive")
    print("=" * 50)
    print(f"URL         : {URL}")
    print(f"Status Code : {response.status_code}")
    print(f"Response    : {response.text[:200]}")
    print("=" * 50)

except requests.exceptions.RequestException as e:
    print("=" * 50)
    print("Failed to reach Render")
    print(f"Error: {e}")
    print("=" * 50)
    raise
