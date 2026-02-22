import requests

BASE_URL = "http://localhost:8000"


def get(path: str):
    try:
        return requests.get(BASE_URL + path)
    except:
        return None


def post(path: str, json):
    return requests.post(BASE_URL + path, json=json)


def put(path: str, json):
    return requests.put(BASE_URL + path, json=json)


def put_file(path: str, files):
    return requests.put(BASE_URL + path, files=files)
