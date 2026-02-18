from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class GenreRead(GenreBase):
    id: int

    class config:
        from_attributes = True

    def to_payload(row) -> GenreRead:
        return {
            "id": row[0],
            "name": row[1]
        }
