from fastapi import APIRouter, Depends, HTTPException, status
from src.backend.fastapi.security import OAuth2PasswordRequestForm
from src.backend.services.auth_service import authenticate_user, create_access_token
from src.backend.models.token import Token


router = APIRouter(
    prefix="/token",
    tags=["auth"]
)


@router.post("/")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate Credantials", headers={"WWW-Authenticate": "Bearer"})

    access_token = create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
