from pydantic import BaseModel
from backend.type.ProductDto import ProductDto

class ItemsDto(BaseModel):
    customer_id: str
    products: list[ProductDto]