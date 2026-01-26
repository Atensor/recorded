import requests

BASE_URL = "http://localhost:8000"


def get(path: str):
    return requests.get(BASE_URL + path).json()


def post(path: str, json):
    return requests.post(BASE_URL + path, json=json)


def get_file(path: str):
    response = requests.get(BASE_URL + path)
    return (response.headers, response.content)


def put_file(path: str, files):
    return requests.put(BASE_URL + path, files=files)
