import time
import requests
from datetime import datetime

URL = "https://new-ugt0.onrender.com/"

while True:
    try:
        response = requests.get(URL, timeout=30)

        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Status: {response.status_code}"
        )

    except Exception as e:
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Error: {e}"
        )

    # Wait for 10 minutes
    time.sleep(600)