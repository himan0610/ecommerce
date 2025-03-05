from fastapi import FastAPI
from .controller import OrderController, PaymentController, ShippingController
from .service import StatisticService 

app = FastAPI()

app.include_router(OrderController.router)
app.include_router(PaymentController.router)
app.include_router(ShippingController.router)


@app.get("/stats")
async def root():
    return StatisticService.get_statistics()