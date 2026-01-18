import json

# TODO: implement with backend

records = ({"id": 1, "title": "White Pony", "artist": "Deftones",
            "label": "Maveric", "genre": "Nu Metal", "year": 2000,
            "image": "https://m.media-amazon.com/images/I/51BXwSNRwIL._SL1425_.jpg"},
           {"id": 2, "title": "Paranoid", "artist": "Black Sabbath",
            "label": "Sanctuary", "genre": "Metal", "year": 1970,
            "image": "https://i.scdn.co/image/ab67616d00001e029683e5d7361bb80bfb00f46d"})

tracks = {1: {'id': 1, 'nr': 1, 'record': 1, 'title': 'track 1'},
          2: {'id': 2, 'nr': 2, 'record': 1, 'title': 'track 2'},
          3: {'id': 3, 'nr': 3, 'record': 1, 'title': 'track 3'},
          4: {'id': 4, 'nr': 4, 'record': 1, 'title': 'track 4'},
          5: {'id': 5, 'nr': 5, 'record': 1, 'title': 'track 5'},
          6: {'id': 6, 'nr': 6, 'record': 1, 'title': 'track 6'},
          7: {'id': 7, 'nr': 7, 'record': 1, 'title': 'track 7'},
          8: {'id': 8, 'nr': 8, 'record': 1, 'title': 'track 8'},
          9: {'id': 9, 'nr': 9, 'record': 1, 'title': 'track 9'},
          10: {'id': 10, 'nr': 10, 'record': 1, 'title': 'track 10'},
          11: {'id': 11, 'nr': 1, 'record': 2, 'title': 'track 11'},
          12: {'id': 12, 'nr': 2, 'record': 2, 'title': 'track 12'},
          13: {'id': 13, 'nr': 3, 'record': 2, 'title': 'track 13'},
          14: {'id': 14, 'nr': 4, 'record': 2, 'title': 'track 14'},
          15: {'id': 15, 'nr': 5, 'record': 2, 'title': 'track 15'},
          16: {'id': 16, 'nr': 6, 'record': 2, 'title': 'track 16'},
          17: {'id': 17, 'nr': 7, 'record': 2, 'title': 'track 17'},
          18: {'id': 18, 'nr': 8, 'record': 2, 'title': 'track 18'},
          19: {'id': 19, 'nr': 9, 'record': 2, 'title': 'track 19'}}


def get_records():
    return records


def get_record(id: int):
    return records[id - 1]


def get_tracks(record_id):
    record_tracks: json = {}

    n_tracks = 0
    for track in tracks:
        if tracks[track]["record"] == record_id:
            n_tracks += 1
            record_tracks[n_tracks] = tracks[track]

    return record_tracks


def get_track(id):
    return tracks[id]


def get_artists():
    artists = [
        {
            "id": 0,
            "name": "Deftones"
        },
        {
            "id": 1,
            "name": "Black Sabbath"
        }
    ]
    artist_dict = {}
    for artist in artists:
        artist_dict[artist["id"]] = artist["name"]
    return artist_dict


def get_labels():
    labels = [
        {
            "id": 0,
            "name": "Maveric"
        },
        {
            "id": 1,
            "name": "Sanctuary"
        }
    ]
    label_dict = {}
    for label in labels:
        label_dict[label["id"]] = label["name"]
    return label_dict


def get_genres():
    genres = [
        {
            "id": 0,
            "name": "Metal"
        },
        {
            "id": 1,
            "name": "Nu Metal"
        }
    ]
    genre_dict = {}
    for genre in genres:
        genre_dict[genre["id"]] = genre["name"]
    return genre_dict
