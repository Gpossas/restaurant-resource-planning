from pydantic import BaseModel, Field, HttpUrl

class Image( BaseModel ):

    url: HttpUrl = Field( ... )
    name: str = Field( ... )