from pydantic import BaseModel

class ProductDto(BaseModel):
    id: str
    quantity: int
    vendor_id: str