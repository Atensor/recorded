from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt


from config import get_oath_secret_key
from services.user_service import get_user_by_name_service, get_user_db_service
from services.hash_service import verify_password
from models.user import UserRead, UserReadDB
from models.token import TokenData


SECRET_KEY = get_oath_secret_key()
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token/")


def authenticate_user(username: str, password: str) -> UserReadDB or bool:
    user = get_user_db_service(username)

    if user is None:
        return False
    if not verify_password(password, user["password_hash"]):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + timedelta
    else:
        expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserRead:
    credential_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail="Could not validate Credantials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exeption

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exeption

    user = get_user_by_name_service(token_data.username)
    if user is None:
        raise credential_exeption

    return user
