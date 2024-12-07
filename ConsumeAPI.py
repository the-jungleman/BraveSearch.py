import requests
import json

class ConsumeAPI:
    def __init__(self):
        pass

    def consume_api(self, query):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
            self.api_key = config['API_KEY']

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "x-subscription-token": self.api_key
            }

            params = {
                "q": query,
                "lang": "pt",
                "count": 10,
            }

            url = "https://api.search.brave.com/res/v1/web/search"
            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Erro ao consumir a API: {e}")
