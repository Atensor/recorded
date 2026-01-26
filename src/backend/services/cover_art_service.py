from platform import system
from os.path import expanduser
from os import makedirs
from fastapi import UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
from models.cover_art import CoverArtCreate
from repositories.cover_art_repo import read_art_path, add_art_path
from services.record_service import get_record_min_service

Path(expanduser("~"), ".local/share/recorded/cover_art/" if system()
     == "linux" else "/AppData/roaming/recorded/cover_art/")
BASE_PATH = "/home/bent/.local/share/recorded/cover_art/"


def get_cover_art_service(record_id: int) -> FileResponse:
    row = read_art_path(record_id)
    return FileResponse(
        path=row[0],
        media_type="image/png",
        filename=row[0].split("/")[7])


def add_art(record_id: int, content: UploadFile, filename: str):
    record = get_record_min_service(record_id)
    path = Path(
        BASE_PATH +
        f"{record["artist"]["name"]}/{filename}")
    makedirs(Path(BASE_PATH + record["artist"]["name"]))
    with open(path, "xb") as i:
        i.write(content)
    add_art_path(record_id, str(path))
