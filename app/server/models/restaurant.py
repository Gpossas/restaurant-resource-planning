from datetime import time
from pydantic import BaseModel, Field
from models.image import Image
from models.adress import Adress
from models.dishes import Dishes


class RestaurantSchema( BaseModel ):

    cnpj: str = Field( primary_key=True, min_length=14, max_length=14 )
    name: str = Field( ... )    
    category: str = Field( ... )
    adress: Adress = Field( ... )
    dishes: Dishes = Field( ... )
    description: str | None
    logo: Image | None
    opening_hours : dict[list[time]] | None
    payment_methods: list[str] | None

    
    model_config = {
        "json_schema_extra": {
            "examples": {
                "cnpj": "12.345.678/0001-00",
                "name": "Morama",
                "category": "Candy store",
                "adress": {
                    "street": "Somewhere over the rainbow, 12",         
                    "complement": "High above the chimney tops"
                },
                "dishes": [
                    {
                        "name": "chocolate cake",
                        "price": 316.23
                    },
                    {
                        "name": "vanilla ice cream",
                        "price": 9.99
                    },
                ],
                "description": "Morama is a candy shop that was created by 3 friends in 2024",
                "logo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wfla.com%2Fbloom-tampa-bay%2F10-surprising-benefits-of-having-a-cat-in-your-life%2F&psig=AOvVaw0TUkLGDFWdSmBOfDe38731&ust=1708977051859000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOiZuuKhx4QDFQAAAAAdAAAAABAE",
                "opening_hours": {
                    "monday": [ ( time(7, 0), time(11, 45) ), ( time(14, 0), time(6, 0)) ],
                    "tuesday": [ ( time(7, 0), time(11, 45) ), ( time(14, 0), time(6, 0)) ],
                    "wednesday": [ ( time(7, 0), time(11, 45) ), ( time(14, 0), time(6, 0)) ],
                    "thursday": [ ( time(7, 0), time(11, 45) ), ( time(14, 0), time(6, 0)) ],
                    "friday": [ ( time(7, 0), time(11, 45) ), ( time(14, 0), time(6, 0)) ],
                    "saturday": [ ( time(7, 0), time(12, 0) ) ],
                    "sunday": [],
                },
                "opening_hours": ["Pix", "Credit card"]
            }
        }
    }