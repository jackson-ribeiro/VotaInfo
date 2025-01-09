import requests
from config import API_URL

def get_locais_votacao():
    response = requests.get(f"{API_URL}locaisvotacao")
    return response.json()

def get_locais_votacao_bairro(bairro):
    response = requests.get(f"{API_URL}locaisvotacao/bairro/{bairro}")
    return response.json()

def get_locais_votacao_municipio(municipio):
    response = requests.get(f"{API_URL}locaisvotacao/municipio/{municipio}")
    return response.json()

def get_locais_votacao_zona(zona):
    response = requests.get(f"{API_URL}locaisvotacao/zona/{zona}")
    return response.json()