import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config


MONGO_DETAILS = config( "MONGO_DETAILS" )
client = motor.motor_asyncio.AsyncIOMotorClient( MONGO_DETAILS )
database = client.morama
food_collection = database.get_collection( "foods" )


# helpers


def food_helper( food ) -> dict:
    return {
        "id": str( food["_id"] ),
        'name': food['name'],
        'price': food['price'],
        'ingredients': food['ingredients'],
        'extras': food['extras'],
        'kcal': food['kcal'],
        'is_vegan': food['is_vegan'],
        'is_vegetarian': food['is_vegetarian'],
        'is_lactose_free': food['is_lactose_free'],
    }


# Retrieve all foods present in the database
async def retrieve_foods():
    foods = []
    async for food in food_collection.find():
        foods.append(food_helper(food))
    return foods


# Add a new food into to the database
async def add_food(food_data: dict) -> dict:
    food = await food_collection.insert_one(food_data)
    new_food = await food_collection.find_one({"_id": food.inserted_id})
    return food_helper(new_food)


# Retrieve a food with a matching ID
async def retrieve_food(id: str) -> dict:
    food = await food_collection.find_one({"_id": ObjectId(id)})
    if food:
        return food_helper(food)


# Update a food with a matching ID
async def update_food(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    
    food = await food_collection.find_one({"_id": ObjectId(id)})
    if food:
        updated_food = await food_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_food:
            return True
        return False


# Delete a food from the database
async def delete_food(id: str):
    food = await food_collection.find_one({"_id": ObjectId(id)})
    if food:
        await food_collection.delete_one({"_id": ObjectId(id)})
        return True