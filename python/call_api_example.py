import requests
import json

def call_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Request failed: {response.status_code}")

if __name__ == "__main__":
    call_api()