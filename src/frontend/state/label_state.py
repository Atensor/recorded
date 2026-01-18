class LabelFormState:
    name: str | None

    def __init__(self):
        self.name = None

    def to_payload(self):
        return {
            "name": self.name
        }

    def is_valid(self) -> bool:
        return bool(self.name)
