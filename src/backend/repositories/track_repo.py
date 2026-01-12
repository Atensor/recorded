from db.database import get_connection
from models.track import TrackCreate


def read_record_tracks(record_id: int):
    con = get_connection()
    return con.execute(f"""
    select
        id, 
        title,
        record_id,
        track_nr
    from 
        tracks
    where
        record_id = {record_id}
    order by track_nr desc
    """).fetchall()


def read_track(id: int):
    con = get_connection()
    return con.execute(f"""
    select
        id, 
        title, 
        record_id
    from
        tracks
    where
        id = {id}
    """).fetchone()


def write_track(track: TrackCreate, record_id: int):
    con = get_connection()
    con.execute(f"""
    insert into tracks values(
        nextval('seq_tid'),
        '{track.title}',
        {record_id},
        {track.tracknr}
    """)
