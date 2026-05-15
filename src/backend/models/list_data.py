from pydantic import BaseModel
from datetime import date


class ListData(BaseModel):
    title: str
    user_id: int


class ListDataFull(ListData):
    description: str | None = None
    last_updated: date


class ListDataRead(ListData):
    id: int

    class config:
        from_attributes = True

    def to_payload(row) -> ListDataRead:
        return {
            "id": row[0],
            "title": row[1],
            "user_id": row[3],
        }


class ListDataFullRead(ListDataFull):
    id: int

    class config:
        from_attributes = True

    def to_payload(row) -> ListDataFullRead:
        return {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "user_id": row[3],
            "last_updated": row[4]
        }
