from dotenv import get_key
from pathlib import Path

ENVIRONMENT_VARIABLE = "OAUTH_SECRET_KEY"

ERROR_TEXT = f'''{ENVIRONMENT_VARIABLE} needs to be set
to do so run this command:
export {ENVIRONMENT_VARIABLE}=$(openssl rand -hex 32)'''


def get_oath_secret_key() -> str:
    key = get_key(dotenv_path=Path(Path(__file__).parent.resolve(), ".env"),
                  key_to_get=ENVIRONMENT_VARIABLE)

    if key:
        return key

    raise RuntimeError(ERROR_TEXT)
