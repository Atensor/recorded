from models.label import LabelCreate, LabelRead
from repositories.label_repo import read_labels, read_label, insert_label


def get_labels_service() -> list[LabelRead]:
    rows = read_labels()
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def get_label_service(id: int) -> LabelRead:
    row = read_label(id)
    return {
        "id": row[0],
        "name": row[1]
    }


def create_label_service(label: LabelCreate):
    insert_label(label)
