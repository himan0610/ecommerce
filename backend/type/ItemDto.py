from pydantic import BaseModel
from ProductDto import ProductDto

class ItemsDto(BaseModel):
    customer_id: str
    products: list[ProductDto]