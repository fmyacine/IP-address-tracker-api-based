import uuid
import requests

def apiFirst():
    url = "https://api.ipify.org/?format=json"

    try:
        response = requests.get(
            url,
            cookies={"session": str(uuid.uuid4())},
            headers={"Accept": "*/*", "User-Agent": "python-requests"},
        )
        response.raise_for_status()

        result = response.json()
        return result
    except (KeyError, IndexError, ValueError,requests.exceptions.HTTPError,requests.exceptions.ConnectionError):
        return None



def apiSearch(query):
    url = f"http://ip-api.com/json/{query}?fields=regionName,city,zip,timezone,offset,isp,query"

    try:
        response = requests.get(
            url,
            cookies={"session": str(uuid.uuid4())},
            headers={"Accept": "*/*", "User-Agent": "python-requests"},
        )
        response.raise_for_status()

        result = response.json()
        return result
    except (KeyError, IndexError, ValueError,requests.exceptions.HTTPError,requests.exceptions.ConnectionError):
        return None
