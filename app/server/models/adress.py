from pydantic import Field, BaseModel

class Adress( BaseModel ):

    cep: str = Field( ... )
    street: str = Field( ... )
    residence_number: int = Field( ... )
    neighborhood: str = Field( ... )
    city: str = Field( ... )
    state: str = Field( ... )
    complement: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": {
                "cep": "60130240",
                "street": "Rua Dr. Oswaldo Cruz",
                "residence_number": 476,
                "neighborhood": "Bebedouro",
                "city": "Maceio",
                "state": "AL",
                "complement": "De 2 Até 1550 Lado Par",
            }
        }
    }