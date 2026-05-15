import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.backend.controllers.artist import router as artist_router
from src.backend.controllers.genre import router as genre_router
from src.backend.controllers.label import router as label_router
from src.backend.controllers.record import router as record_router
from src.backend.controllers.track import router as track_router
from src.backend.controllers.user import router as user_router
from src.backend.controllers.auth import router as auth_router

BASE_PATH = "/home/bent/.local/share/recorded/cover_art/"
app = FastAPI()

app.mount("/cover_art", StaticFiles(directory=BASE_PATH), "cover_art")


app.include_router(artist_router)
app.include_router(genre_router)
app.include_router(label_router)
app.include_router(record_router)
app.include_router(track_router)
app.include_router(user_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0", port=8000, log_level="info")
