import requests
import json
response = json.loads(requests.post("https://apis.paralleldots.com/v3/sentiment", data={ "api_key": "h1fPGh0H5LvtHU5LhaEnlhITrHLPSYNHbZTsyusz51s", "text": "#keepfamiliestogether I hate government for doing this."}).text)
print(response)