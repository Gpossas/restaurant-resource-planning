from bson import ObjectId
from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from server.models.restaurant import (
    RestaurantSchema,
    UpdateRestaurant,
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


@router.put( 
    "/{slug}/{id}", 
    response_description="Update a restaurant",
    status_code=status.HTTP_202_ACCEPTED
)
async def update_restaurant_data( 
    id: str, 
    slug: str,
    restaurant: UpdateRestaurant = Body( ... ) 
):
    update_data = {
        k: v for k, v in restaurant.model_dump( by_alias=True ).items() if v is not None
    }
    if len( update_data ) < 1:
        return HTTPException( status.HTTP_422_UNPROCESSABLE_ENTITY, detail='at leat 1 field must be updated' )
    
    restaurant = await restaurant_collection.find_one( { '_id': ObjectId( id ) } )
    if not restaurant:
        return HTTPException( status.HTTP_404_NOT_FOUND, detail="restaurant doesn't exist" )
    
    await restaurant_collection.update_one( 
        { '_id': ObjectId( id ) },
        { '$set': update_data } 
    ) 

    return {
        "successfully updated data": update_data
    }


@router.delete( 
    "/{slug}/{id}", 
    response_description="Delete a restaurant",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_restaurant_data( 
    id: str, 
    slug: str,
):
    restaurant = restaurant_collection.find_one( { '_id': ObjectId( id ) } )
    if not restaurant:
        return HTTPException( status.HTTP_404_NOT_FOUND, detail="restaurant doesn't exist" )
    
    await restaurant_collection.delete_one( { '_id': ObjectId( id ) } )