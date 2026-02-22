from os import getenv
from secrets import token_hex

ENVIRONMENT_VARIABLE = "STORAGE_SECRET_KEY"


def get_storage_secret_key() -> str:
    key = getenv(ENVIRONMENT_VARIABLE)

    # If no key is set a temporary key is generated
    if key is None:
        key = token_hex(32)
        print("No Global Key is set")
    return key
