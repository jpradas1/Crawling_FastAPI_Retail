from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    _id: Optional[str]
    id: Optional[int]
    title: str
    description: str
    brand: str
    inventory: str
    colors: str
    current_price: str
    original_price: str
    size: list
    url_pictures: list
    category_path: list

class Category(BaseModel):
    _id: Optional[str]
    distinctWords: list