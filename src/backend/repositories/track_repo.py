from db.database import get_connection
from models.track import TrackCreate


def read_record_tracks(record_id: int):
    con = get_connection()
    return con.execute("""
    select
        id, 
        title,
        track_nr,
        duration
    from 
        tracks
    where
        record_id = ?
    order by track_nr
    """, [record_id]).fetchall()


def read_track(id: int):
    con = get_connection()
    return con.execute("""
    select
        id, 
        title, 
        record_id,
        track_nr,
        duration
    from
        tracks
    where
        id = ?
    """, [id]).fetchone()


def read_track_record(id: int):
    con = get_connection()
    return con.execute("""
    select
        record_id
    from
        tracks
    where
        id = ?
    """, [id]).fetchone()


def write_record_track(track: TrackCreate, record_id):
    con = get_connection()
    return con.execute("""
    insert into tracks values (
        nextval('seq_tid'),
        ?,
        ?,
        ?,
        ?
    )
    returning
        id,
        track_nr
    """, [track.title, record_id, track.track_nr, track.duration]).fetchone()


def delete_record_tracks(record_id: int):
    con = get_connection()
    con.execute("""
    delete from
        lyrics
    using
        lyrics 
    join 
        tracks
    on
        lyrics.track_id = tracks.id
    where
        tracks.record_id = ?;
    """, [record_id])
    con.execute("""
    delete from
        track_features
    using
        track_features
    join
        tracks
    on
        track_features.track_id = tracks.id
    where
        tracks.record_id = ?;
    """, [record_id])
    con.execute("""
    delete from
        tracks
    where
        record_id = ?;
    """, [record_id])
