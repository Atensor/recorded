from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str


class ArtistCreate(ArtistBase):
    pass


class ArtistRead(ArtistBase):
    id: int

    class config:
        from_attributes = True
