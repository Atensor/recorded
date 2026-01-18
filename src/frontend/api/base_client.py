import requests

BASE_URL = "http://localhost:8000"


def get(path: str):
    return requests.get(BASE_URL + path).json()


def post(path: str, json):
    return requests.post(BASE_URL + path, json=json).json
