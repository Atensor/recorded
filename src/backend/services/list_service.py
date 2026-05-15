from src.backend.models.list_data import ListDataFull, ListDataFullRead, ListDataRead
from src.backend.repositories.list_repo import read_users_list_data, read_list_data, insert_list_data, add_list_record, remove_list


def get_users_lists_service(user_id: int) -> list[ListDataRead]:
    rows = read_users_list_data(user_id)
    return [
        ListDataRead.to_payload(row) for row in rows
    ]


def get_list_service(id: int) -> ListDataFullRead:
    row = read_list_data(id)
    return ListDataFullRead.to_payload(row)


def create_list_service(list_data: ListDataFull):
    insert_list_data(list_data)


def add_list_record_service(list_id: int, record_id: int):
    add_list_record(list_id, record_id)


def remove_list_service(id: int):
    remove_list(id)
