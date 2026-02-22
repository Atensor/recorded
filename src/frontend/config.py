from dotenv import get_key

ENVIRONMENT_VARIABLE = "STORAGE_SECRET_KEY"

ERROR_TEXT = f'''{ENVIRONMENT_VARIABLE} needs to be set
to do so run this command:
echo "{ENVIRONMENT_VARIABLE}=$(openssl rand -hex 32)" > .env'''


def get_storage_secret_key() -> str:
    key = get_key(".env", ENVIRONMENT_VARIABLE)

    if key:
        return key

    raise RuntimeError(ERROR_TEXT)
