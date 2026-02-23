from models.user_records import User_RecordBase
from models.rating import RecordRatingBase
from repositories.user_record_repo import read_record_users, read_user_record_ids, read_user_records, insert_user_record, delete_user_record


def get_record_user_ids_service(record_id: int) -> list[int]:
    return read_record_users(record_id)


def get_user_record_ids_service(user_id: int) -> list[int]:
    return read_user_record_ids(user_id)


def get_user_records_service(user_id: int) -> list[User_RecordBase]:
    rows = read_user_records(user_id)
    return [
        User_RecordBase(**User_RecordBase.to_payload(row)) for row in rows
    ]


def add_record_tag_service(user_record: User_RecordBase):
    insert_user_record(user_record)


def delete_record_tag_service(user_record: User_RecordBase):
    delete_user_record(user_record)
