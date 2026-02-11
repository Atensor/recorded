from models.track import TrackCreate, TrackRead
from repositories.track_repo import read_record_tracks, read_track, read_track_record, write_record_track, delete_record_tracks
from services.artist_service import get_track_features_service, add_track_features_service


def get_record_tracks_service(record_id: int) -> list[TrackRead]:
    rows = read_record_tracks(record_id)
    return [
        {
            "id": row[0],
            "title": row[1],
            "track_nr": row[2],
            "duration": row[3],
            "features": get_track_features_service(row[0])
        } for row in rows
    ]


def get_track_service(id: int) -> TrackRead:
    row = read_track(id)
    return {
        "id": row[0],
        "title": row[1],
        "record_id": row[2],
        "track_nr": row[3],
        "duration": row[4],
        "features": get_track_features_service(row[0])
    }


def get_track_record_id_service(id: int) -> int:
    return read_track_record(id)[0]


def create_record_tracks_service(tracks: list[TrackCreate], record_id: int):
    for track in tracks:
        row = write_record_track(track, record_id)

        if track.feature_ids:
            add_track_features_service(row[0], track.feature_ids)


def delete_record_tracks_service(record_id: int):
    delete_record_tracks(record_id)
