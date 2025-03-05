from fastapi import APIRouter, HTTPException
from backend.service import OrderService
from backend.type import ItemDto

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("/")
async def create(items: ItemDto):
    OrderService.create(items)
    return {"message": "Order will be placed in sometime"}

@router.get("/{id}")
async def get(id: str):
    response = OrderService.getById(id)
    if response == None or len(response) == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return response

