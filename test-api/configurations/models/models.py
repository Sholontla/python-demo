import os
from datetime import datetime
from typing import Dict, Optional, List, Dict
from pydantic import BaseModel
from pydantic.networks import stricturl

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from configurations import Base

class SqlData(Base):
    __tablename__ = "sqldata"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category = Column(String)
    sub_category = Column(String)
    product = Column(String)
    price = Column(Integer, default=0)
    quantity = Column(Integer, default=0)
    total = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('userssql.id'))

    creator = relationship("UserSql", back_populates="datasql")

class UserSql(Base):
    __tablename__ = "userssql"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    blog = relationship("SqlData", back_populates="creator")




