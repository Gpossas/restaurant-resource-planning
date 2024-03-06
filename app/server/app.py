from fastapi import FastAPI

from server.routes.food import router as FoodRouter
from server.routes.restaurant import router as RestaurantRouter

app = FastAPI()

app.include_router(FoodRouter, tags=["Food"], prefix="/food")
app.include_router(RestaurantRouter, tags=["Restaurant"], prefix="/restaurants")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello world!"}