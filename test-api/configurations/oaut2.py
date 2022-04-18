from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from configurations.configuration_variables import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from configurations.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No't validate credentials",
        headers={"No Access": "Forbidden"},
    )
    return verify_token(data, credentials_exception)


