from typing import List, Dict, Optional
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import asyncio, motor



class Category(BaseModel):
    category: str

class SubCategory(BaseModel):
    subcategory: str

class ProductSerieNumber(BaseModel):
    serial_number: int

class Product(BaseModel):
    category: Category
    subCategory: SubCategory
    productSerieNumber: ProductSerieNumber
    product: str
    price: int



