import json
import urllib.request

def fetch_gigs():
    url = "http://localhost:3000/verify"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read().decode())
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error fetching endpoint: {e}")

if __name__ == "__main__":
    fetch_gigs()
