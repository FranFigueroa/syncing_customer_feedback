import requests


class DataFetcher:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos del sistema externo: {e}")
            return []

