class ArtistFormState:
    name: str | None

    def __init__(self):
        self.name = None

    def to_payload(self) -> dict:
        return {
            "name": self.name
        }

    def is_valid(self) -> bool:
        return bool(self.name)


class ArtistState:
    id: int | None
    name: str | None

    def __init__(self, artist_dict):
        self.id = artist_dict["id"]
        self.name = artist_dict["name"]

    def to_payload(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def is_valid(self) -> bool:
        return bool(self.name and self.id)
