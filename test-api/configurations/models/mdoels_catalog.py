import os
from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from configurations import Base

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    categories = relationship("Product", back_populates="category")

class SubCategory(Base):
    __tablename__ = "subcategory"
    id = Column(Integer, primary_key=True, index=True)
    sub_category = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    sub_categories = relationship("Product", back_populates="sub_category")

class SerialNumber(Base):
    __tablename__ = "serial_number"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(Integer, default=0)
    product_id = Column(Integer, ForeignKey('products.id'))
    serial_numbers = relationship("Product", back_populates="serail_number")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    category = relationship("Category", back_populates="categories")
    sub_category = relationship("SubCategory", back_populates="sub_categories")
    serail_number = relationship("SerialNumber", back_populates="serial_numbers")
    product = Column(String)
    price = Column(Integer, default=0)




