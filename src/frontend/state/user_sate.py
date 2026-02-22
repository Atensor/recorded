class UserFormState:
    username: str | None
    password: str | None

    def __init__(self):
        self.username = None
        self.password = None

    def to_payload(self):
        return {
            "username": self.username,
            "password": self.password
        }

    def is_valid(self) -> bool:
        return bool(self.username and self.password)
