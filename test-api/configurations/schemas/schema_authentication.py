from typing import List, Dict, Optional
from pydantic import BaseModel


class SchemaAuthentication(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token = str
    token_type = str

class TokenData(BaseModel):
    email: Optional[str] = None