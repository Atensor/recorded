class TrackFormState:
    title: str | None
    track_nr: int
    feature_ids: list[int]
    minutes: int
    seconds: int

    def __init__(self, track_nr):
        self.title = None
        self.track_nr = track_nr
        self.feature_ids = []
        self.minutes = 0
        self.seconds = 0

    def to_payload(self):
        return {
            "title": self.title,
            "track_nr": self.track_nr,
            "feature_ids": self.feature_ids,
            "duration": self.minutes * 60 + self.seconds
        }

    def is_valid(self) -> bool:
        return bool(self.title and self.track_nr and self.minutes + self.seconds > 0)
