from pydantic import BaseModel, Field

# Just a dish template, this need to be updated
# TODO: make dishes different for each category
class Dish( BaseModel ):

    name: str = Field( ... )
    price: float = Field( ..., gt=0 )
    quantity: int = Field( ..., ge=1 )
    description: str | None = None
    observations: str | None = None
    extras: list[str] | None = None
    ingredients: list[str]