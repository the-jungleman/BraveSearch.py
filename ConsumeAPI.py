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
                "x-subscription-token": self.api_key  # Adiciona o token de assinatura
            }

            params = {
                "q": query,
                "lang": "pt",
                "count": 10,
            }

            url = "https://api.search.brave.com/res/v1/web/search"

            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:
                print(response.json()) 
            else:
                print(f"Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao consumir a API: {e}")

if __name__ == "__main__":
    api = ConsumeAPI()
    api.consume_api("brave search")