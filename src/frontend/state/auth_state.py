from nicegui import app


class TokenState:
    access_token: str
    token_type: str

    def __init__(self, response_data: dict):
        self.access_token = response_data["access_token"]
        self.token_type = response_data["token_type"]

    def to_payload(self) -> str:
        return f"{self.token_type.capitalize()} {self.access_token}"


def set_token(token: TokenState):
    app.storage.user["token"] = token


def get_token() -> TokenState | None:
    return TokenState(**app.storage.user.get("token"))


def clear_token():
    app.storage.user.clear()
