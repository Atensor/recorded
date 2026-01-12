import uvicorn
from fastapi import FastAPI
from controllers.artist import router as artist_router
from controllers.genre import router as genre_router
from controllers.label import router as label_router
from controllers.record import router as record_router
from controllers.track import router as track_router

app = FastAPI()

app.include_router(artist_router, prefix=("/artists"), tags=["Artist"])
app.include_router(genre_router)
app.include_router(label_router)
app.include_router(record_router)
app.include_router(track_router)

if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0", port=8000, log_level="info")
