from typing import List, Dict, Optional
from pydantic import BaseModel

class SchemaBlogBase(BaseModel):
    title: str
    body: str

class SchemaBlog(SchemaBlogBase):
    class Config():
        orm_mode = True

class SchemaUser(BaseModel):
    username: str
    password: str
    email: str

class SchemaShowUser(BaseModel):
    username: str
    email: str
    blog: List[SchemaBlog] = []
    class Config():
        orm_mode = True

class SchemaShowBlog(BaseModel):
    title: str
    body: str
    creator: SchemaShowUser
    class Config():
        orm_mode = True

class Title(BaseModel):
    title: str

class Currencies(BaseModel):
    id: int
    curency_usd: str
    curency_eu: str
    curency_mx: str

class Description(BaseModel):
    description: str

class Products(BaseModel):
    product: str
    category: str

class Price(BaseModel):
    products: Products
    price: int

class Quantity(BaseModel):
    products: Price
    product: int

class Payer(BaseModel):
    name: str
    email: str
    idetnification: Dict


class Address(BaseModel):
    street: str
    conutry: str = 'USA'
    zipcode: str


class SchemaAuthentication(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token = str
    token_type = str

class TokenData(BaseModel):
    email: Optional[str] = None