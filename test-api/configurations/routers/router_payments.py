
from asgiref.typing import HTTPRequestEvent
import motor
import asyncio
from typing import List
from fastapi import APIRouter, responses, status, Response, HTTPException, Depends
from beanie import init_beanie
from beanie import PydanticObjectId

from configurations import get_db
from configurations.oaut2 import get_current_user
from schemas.schemas import SchemaUser
from schemas.schemas_payments import SchemasPayments, Payments, AggregationResponseItem
from repositroy.repo_payments import create_payment, get_payment_by_id
from configurations.configuration_variables import MONGO_PORT, MONGO_PORT, MONGO_HOST, MONGO_ADMIN_USER, MONGO_ADMIN_PASSWORD
from beanie import init_beanie


router_payments = APIRouter()

@router_payments.post('/', status_code=status.HTTP_201_CREATED, response_model=SchemasPayments)
async def auth_post_payment(request: Payments):#, get_current_user: SchemaUser = Depends(get_current_user)):
    return create_payment(request)

# @router_payments.get('/', response_model = List[SchemasPayments])
# async def auth_get_all_blog_users(get_current_user: Payments):
#     return await Cocktail.find_all().to_list()

# @router_payments.get('/{id_payments}', status_code = 200, response_model = SchemasPayments)
# def auth_get_by_id_blog_user(id_payments: int, get_current_user: SchemaUser = Depends(get_current_user)):
#     return get_payment_by_id(id_payments)

# @router_payments.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def auth_update_by_id_blog_user(id: int, router: SchemaBlog, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
#     return put_blog(id, router, db)

# @router_payments.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def auth_delete_by_id_blog_user(id: int, db: Session = Depends(get_db), get_current_user: SchemaUser = Depends(get_current_user)):
#     return delete_blog(id, db)

