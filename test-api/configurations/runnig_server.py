import motor
import uvicorn
from fastapi import FastAPI
from beanie import init_beanie
from pydantic import BaseSettings
from routers.router_authentication import router_authentication
from routers.routers_users import router_users
from routers.routers_blog import router_blog
from routers.router_payments import router_payments
from routers.routers_catalog import router_catalog
from schemas.schemas_payments import Payments

from models import models
from configurations.configuration_variables import API_SERVER_HOST, API_SERVER_PORT
from configurations.db_connections import Base, engine

app = FastAPI(
    title = "FastApi",
    description = "postgreSql and mongoDB",
    version = "0.0.0 / test",
)

models.Base.metadata.create_all(bind=engine)

app.include_router(router_authentication)
app.include_router(router_users)
app.include_router(router_blog)
app.include_router(router_catalog, prefix="/catalog", tags=["Catalog"])
# app.include_router(router_payments, prefix="/payments", tags=["PAYMENS"])

def config_server():
    return uvicorn.run(app, host = API_SERVER_HOST, port = int(API_SERVER_PORT), log_level="info")
 