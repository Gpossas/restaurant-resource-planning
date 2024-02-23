from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_food,
    delete_food,
    retrieve_food,
    retrieve_foods,
    update_food,
)
from server.models.food import (
    ErrorResponseModel,
    ResponseModel,
    FoodSchema,
    UpdateFoodModel,
)

router = APIRouter()


@router.post("/", response_description="Food data added into the database")
async def add_food_data(food: FoodSchema = Body(...)):
    food = jsonable_encoder(food)
    new_food = await add_food(food)
    return ResponseModel(new_food, "Food added successfully.")


@router.get("/", response_description="Foods retrieved")
async def get_foods():
    foods = await retrieve_foods()
    if foods:
        return ResponseModel(foods, "Foods data retrieved successfully")
    return ResponseModel(foods, "Empty list returned")


@router.get("/{id}", response_description="food data retrieved")
async def get_food_detail(id):
    food = await retrieve_food(id)
    if food:
        return ResponseModel(food, "Food data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Food doesn't exist.")


@router.put("/{id}")
async def update_food_data(id: str, req: UpdateFoodModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_food = await update_food(id, req)
    if updated_food:
        return ResponseModel(
            f"Food with ID: {id} name update is successful",
            "Food name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the food data.",
    )


@router.delete("/{id}", response_description="Food data deleted from the database")
async def delete_food_data(id: str):
    deleted_food = await delete_food(id)
    if deleted_food:
        return ResponseModel(
            F"Food with ID: {id} removed", "Food deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"Food with id {id} doesn't exist"
    )