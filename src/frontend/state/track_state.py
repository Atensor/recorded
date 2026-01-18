class TrackFormState:
    title: str | None
    tracknr: int
    feature_ids: list[int]

    def __init__(self, tracknr):
        self.title = None
        self.tracknr = tracknr
        self.feature_ids = []

    def to_payload(self):
        return {
            "title": self.title,
            "tracknr": self.tracknr,
            "feature_ids": self.feature_ids
        }

    def is_valid(self) -> bool:
        return bool(self.title and self.tracknr)
