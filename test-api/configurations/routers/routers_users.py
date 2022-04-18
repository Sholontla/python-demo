from asgiref.typing import HTTPRequestEvent
import asyncio
from typing import List
from fastapi import APIRouter, responses, status, Response, HTTPException , Depends
from sqlalchemy.orm import Session

from starlette import requests
from configurations import SessionLocal, get_db

from models.models import UserSql
from schemas.schemas import SchemaUser, SchemaShowUser
from repositroy.repo_user import create_user, get_user, put_user
from configurations.oaut2 import get_current_user
from configurations.hashing import HashAuthentication


router_users = APIRouter(
    prefix="/user",
    tags = ["USERS"]
)


@router_users.post("/", response_model=SchemaShowUser)
def post_create_user(request: SchemaUser, db: Session = Depends(get_db)): #, get_current_user: SchemaUser = Depends(get_current_user)):
    new_user = UserSql(username = request.username, password = HashAuthentication.bcryptHasshing(request.password), email = request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_user

@router_users.get("/{id}", response_model=SchemaShowUser)
def get_by_id_user(id: int, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return get_user(id, db)

@router_users.put("/{id}")
def put_by_id_user(id: int, request: SchemaUser, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return put_user(id, request, db)
