from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.restaurant import (
    RestaurantSchema,
    restaurant_serializer
)
from server.database import restaurant_collection

router = APIRouter()

@router.post( "/create", response_description="You created a restaurant! 🏠🍽️" )
async def create_restaurant( restaurant: RestaurantSchema = Body( ... ) ):
    restaurant = jsonable_encoder( restaurant )
    new_restaurant = await restaurant_collection.insert_one( restaurant )
    return restaurant_serializer( await restaurant_collection.find_one( { '_id': new_restaurant.inserted_id } ) )


@router.get( "/", response_description="See all restaurants nearby! 🏠🍽️" )
async def get_restaurants():
    restaurants = []
    for document in await restaurant_collection.find().to_list( length=100 ):
        restaurants.append( restaurant_serializer(document) )
    return restaurants

