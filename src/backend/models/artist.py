from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str


class ArtistCreate(ArtistBase):
    pass


class ArtistRead(ArtistBase):
    id: int

    class config:
        from_attributes = True

    def to_payload(row) -> ArtistRead:
        return {
            "id": row[0],
            "name": row[1]
        }
