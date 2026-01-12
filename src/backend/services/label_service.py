from repositories.label_repo import read_label, write_label


def get_label(id: int):
    row = read_label(id)
    return {
        "id": row[0],
        "name": row[1]
    }


def create_label(label):
    write_label(label)
