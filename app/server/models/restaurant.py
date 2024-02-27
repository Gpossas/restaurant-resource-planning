from datetime import time
from pydantic import BaseModel, Field
from server.models.image import Image
from server.models.address import Address
from server.models.dish import Dish, PyObjectId


class RestaurantSchema( BaseModel ):

    id: PyObjectId = Field( default_factory=PyObjectId, alias="_id" )
    cnpj: str = Field( ..., min_length=14, max_length=14 )
    name: str = Field( ... )    
    slug: str = Field( ... )
    category: str = Field( ... )
    address: Address = Field( ... )
    # dishes: list[Dish] = Field( ... )
    description: str | None = None
    logo: Image | None = None
    opening_hours : dict[str, list[tuple[time, time]]] | None = None
    payment_methods: list[str] | None = None

    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "cnpj": "12345678000100",
                    "name": "Morama",
                    "slug": "morama",
                    "category": "Candy store",
                    "address": {
                        "cep": "60130240",
                        "street": "Rua Dr. Oswaldo Cruz",
                        "residence_number": 476,
                        "neighborhood": "Bebedouro",
                        "city": "Maceio",
                        "state": "AL",
                        "complement": "De 2 Até 1550 Lado Par",
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
                    "payment_methods": ["Pix", "Credit card"]
                }
            ]       
        }
    }