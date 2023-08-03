from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]
    title: str
    brand: str
    description: str
    pid: Optional[int]
    color: str
    current_price: float
    original_price: float
    currency: str
    inventory: str
    sizes: list
    category_path: str
    URL_images: list
    URL_product: str