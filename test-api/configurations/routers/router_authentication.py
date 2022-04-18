from fastapi import APIRouter, responses, status, Response, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.schema_authentication import SchemaAuthentication
from configurations import SessionLocal, get_db
from configurations.hashing import HashAuthentication
from configurations.token import create_access_token
from models.models import UserSql


router_authentication = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)


@router_authentication.post("/")
def authentication(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserSql).filter(UserSql.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Not Authorize.....")
    if not HashAuthentication.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_405_METHOD_NOT_ALLOWED, detail = f"Not Authorize.....")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}