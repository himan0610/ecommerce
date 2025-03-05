from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.post("/{order_id}")
async def get():
    return {"name": "Test payments"}
