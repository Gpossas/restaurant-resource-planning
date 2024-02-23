from typing import Optional

from pydantic import BaseModel, Field

class FoodSchema( BaseModel ):

    name: str = Field(...)
    price: float = Field( ..., gt=0 )
    ingredients: list[str] = Field( ... )
    extras: list[str] = Field()
    kcal: float = Field( gt=0 )
    is_vegan: bool = Field()
    is_vegetarian: bool = Field()
    is_lactose_free: bool = Field()

    class Config:
        schema_extra = {
            "example": {
                "name": "chocolate cake",
                "price": 39.00,
                "ingredients": ["chocolate", "eggs", "sugar", "milk", "flour"],
                "extras": ["strawberry sauce", "cherry", "rainbow sprinkles"],
                "kcal": 346.56,
                "is_vegan": False,
                "is_vegetarian": False,
                "is_lactose_free": False
            }
        }


class UpdateFoodModel( BaseModel ):

    name: Optional[ str]
    price: Optional[float]
    ingredients: Optional[list[str]]
    extras: Optional[list[str]]
    kcal: Optional[float]
    is_vegan: Optional[bool]
    is_vegetarian: Optional[bool]
    is_lactose_free: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "vegan chocolate cake",
                "price": 46.00,
                "ingredients": ["chocolate", "vegan eggs", "sugar", "not milk", "flour"],
                "extras": ["strawberry sauce", "cherry", "rainbow sprinkles"],
                "kcal": 306.56,
                "is_vegan": True,
                "is_vegetarian": True,
                "is_lactose_free": True
            }
        }


def ResponseModel( data, message ):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel( error, code, message ):
    return {"error": error, "code": code, "message": message}