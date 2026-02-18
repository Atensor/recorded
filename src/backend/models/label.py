from pydantic import BaseModel


class LabelBase(BaseModel):
    name: str


class LabelCreate(LabelBase):
    pass


class LabelRead(LabelBase):
    id: int

    class config:
        from_attributes = True

    def to_payload(row) -> LabelRead:
        return {
            "id": row[0],
            "name": row[1]
        }
