from bson import ObjectId
from fastapi import APIRouter, Body, status, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from utils.database import get_collection
from v1.schemas.restaurant import (
    RestaurantSchema,
    UpdateRestaurant,
    restaurant_serializer
)

router = APIRouter()

@router.post( "/create", response_description="You created a restaurant! 🏠🍽️" )
async def create_restaurant( request: Request, restaurant: RestaurantSchema = Body( ... ) ):
    restaurant = jsonable_encoder( restaurant )
    new_restaurant = await get_collection( request, 'restaurants' ).insert_one( restaurant )
    return restaurant_serializer( await get_collection( request, 'restaurants' ).find_one( { '_id': new_restaurant.inserted_id } ) )


@router.get( "/", response_description="See all restaurants nearby! 🏠🍽️" )
async def get_restaurants( request: Request ):
    restaurants = []
    for document in await get_collection( request, 'restaurants' ).find().to_list( length=100 ):
        restaurants.append( restaurant_serializer(document) )
    return restaurants


@router.put( 
    "/{slug}/{id}", 
    response_description="Update a restaurant",
    status_code=status.HTTP_202_ACCEPTED
)
async def update_restaurant_data( 
    request: Request, 
    id: str, 
    slug: str,
    restaurant: UpdateRestaurant = Body( ... ) 
):
    update_data = {
        k: v for k, v in restaurant.model_dump( by_alias=True ).items() if v is not None
    }
    if len( update_data ) < 1:
        return HTTPException( status.HTTP_422_UNPROCESSABLE_ENTITY, detail='at leat 1 field must be updated' )
    
    restaurant = await get_collection( request, 'restaurants' ).find_one( { '_id': ObjectId( id ) } )
    if not restaurant:
        return HTTPException( status.HTTP_404_NOT_FOUND, detail="restaurant doesn't exist" )
    
    await get_collection( request, 'restaurants' ).update_one( 
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
    request: Request, 
    id: str, 
    slug: str,
):
    restaurant = get_collection( request, 'restaurants' ).find_one( { '_id': ObjectId( id ) } )
    if not restaurant:
        return HTTPException( status.HTTP_404_NOT_FOUND, detail="restaurant doesn't exist" )
    
    await get_collection( request, 'restaurants' ).delete_one( { '_id': ObjectId( id ) } )