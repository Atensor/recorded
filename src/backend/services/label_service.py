from repositories.label_repo import read_labels, read_label, insert_label


def get_labels():
    rows = read_labels()
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def get_label(id: int):
    row = read_label(id)
    return {
        "id": row[0],
        "name": row[1]
    }


def create_label(label):
    insert_label(label)
