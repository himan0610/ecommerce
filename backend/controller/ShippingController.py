from fastapi import APIRouter

router = APIRouter(
    prefix="/shippings",
    tags=["shippings"]
)

@router.patch("/{order_id}")
async def get():
    # TODO: Shipping implementation
    return {"name": "Test Shipping"}
