import requests
from api.base_client import BASE_URL
from state.auth_state import TokenState, set_token, get_token


def get_with_auth(path: str):
    token = get_token()

    headers = {}
    if token:
        headers.update(get_header(token))

    return requests.get(BASE_URL + path, headers=headers)


def post_with_auth(path: str, json: dict | None = None, params: str | None = None):
    token = get_token()

    headers = {}
    if token:
        headers.update(get_header(token))

    return requests.post(BASE_URL + path, json=json, headers=headers, params=params)


def put_with_auth(path: str, json: dict | None = None, params: str | None = None):
    token = get_token()

    headers = {}
    if token:
        headers.update(get_header(token))

    return requests.put(BASE_URL + path, json=json, headers=headers, params=params)


def delete_with_auth(path: str, json: dict | None = None, params: str | None = None):
    token = get_token()

    headers = {}
    if token:
        headers.update(get_header(token))

    return requests.delete(BASE_URL + path, json=json, headers=headers, params=params)


def post_token(user: UserFormState) -> bool:
    payload = user.to_payload()
    payload.update({"grant_type": "password"})

    response = post_data("/token/", payload)
    if response.status_code == 200:
        set_token(response.json())
        return True
    else:
        return False


def post_data(path: str, payload: str):
    return requests.post(BASE_URL + path, data=payload)


def get_header(token: TokenState) -> dict[str, str]:
    return {"Authorization": token.to_payload()}
