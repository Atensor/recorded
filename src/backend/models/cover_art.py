from fastapi import UploadFile
from pydantic import BaseModel
from models.record import RecordReadMin as Record


class File(BaseModel):
    filename: str
    file: bytes


class CoverArtBase(BaseModel):
    record: Record


class CoverArtCreate(CoverArtBase):
    file: File

    class config:
        from_attributes = True
