import requests
from config import API_URL

def get_zonas():
    response = requests.get(f"{API_URL}zonas")
    return response.json()
