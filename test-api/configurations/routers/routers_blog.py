from asgiref.typing import HTTPRequestEvent
from fastapi import APIRouter, responses, status, Response, HTTPException, Depends
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from configurations import get_db
from configurations.oaut2 import get_current_user
from schemas.schemas import SchemaBlog, SchemaShowBlog, SchemaUser
from repositroy.repo_blog import create_blog, get_all, get_blog_by_id, put_blog, delete_blog

router_blog = APIRouter(
    prefix="/blog",
    tags = ["BLOG"]
)

    
@router_blog.post('/', status_code=status.HTTP_201_CREATED)
def auth_post_blog(request: SchemaBlog, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return create_blog(request, db)

@router_blog.get('/', response_model = List[SchemaShowBlog])
def auth_get_all_blog_users(db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return get_all(db)

@router_blog.get('/{id}', status_code = 200, response_model = SchemaShowBlog)
def auth_get_by_id_blog_user(id: int, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return get_blog_by_id(id, db)

@router_blog.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def auth_update_by_id_blog_user(id: int, router: SchemaBlog, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return put_blog(id, router, db)

@router_blog.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def auth_delete_by_id_blog_user(id: int, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
    return delete_blog(id, db)