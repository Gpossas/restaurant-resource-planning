from pydantic import Field, BaseModel
from v1.schemas.address import Address

class ContactSchema( BaseModel ):
  cpf: int = Field( ... )
  reason: str = Field( ... )
  fantasy: str = Field( ... )
  email: str = Field( ... )
  phone: str = Field( ... )
  c_type: str = Field( ... )
  address: Address = Field( ... )

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "cpf": 11222333000144,
          "reason": "Universidade de Maceio",
          "fantasy": "Unima",
          "email": "emailtop@unima.com.br",
          "phone": "(00) 9 0000-0000",
          "c_type": "supplier",
          "address": {
            "cep": "60-130.240",
            "street": "Rua Dr. Oswaldo Cruz",
            "residence_number": 476,
            "neighborhood": "Bebedouro",
            "city": "Maceio",
            "state": "AL",
            "complement": "De 2 Até 1550 Lado Par"
          }
        }
      ]
    }
  }

class UpdateContact( BaseModel ):
  cpf: int | None = None
  reason: str | None = None
  fantasy: str | None = None
  email: str | None = None
  phone: str | None = None
  c_type: str | None = None
  address: Address | None = None


def contact_serializer( contact ) -> dict:
  return {
    "id": str( contact.get('_id')),
    "cpf": contact.get('cpf'),
    "reason": contact.get('reason'),
    "fantasy": contact.get('fantasy'),
    "email": contact.get('email'),
    "phone": contact.get('phone'),
    "c_type": contact.get('c_type'),
    "address": contact.get('address')
  }