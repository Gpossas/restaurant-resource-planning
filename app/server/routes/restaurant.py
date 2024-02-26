from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.restaurant import (
    RestaurantSchema,
)
from server.database import restaurant_collection

router = APIRouter()

@router.post( "/create", response_description="You created a restaurant! 🏠🍽️" )
async def create_restaurant( restaurant: RestaurantSchema = Body( ... ) ):
    restaurant = jsonable_encoder( restaurant )
    new_restaurant = await restaurant_collection.insert_one( restaurant )
    return await restaurant_collection.find_one( { '_id': new_restaurant.inserted_id } )

