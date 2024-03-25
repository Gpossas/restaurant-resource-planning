from pydantic import Field, BaseModel
from v1.schemas.address import Address

class ContactSchema( BaseModel ):
	cpf: int = Field( ... )
	company_name: str = Field( ... )
	trade_name: str = Field( ... )
	email: str = Field( ... )
	phone: str = Field( ... )
	contact_type: str = Field( ... )
	address: Address = Field( ... )

	model_config = {
		"json_schema_extra": {
			"examples": [
				{
					"cpf": 11222333000144,
					"company_name": "Universidade de Maceio",
					"trade_name": "Unima",
					"email": "emailtop@unima.com.br",
					"phone": "(00) 9 0000-0000",
					"contact_type": "supplier",
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
  company_name: str | None = None
  trade_name: str | None = None
  email: str | None = None
  phone: str | None = None
  contact_type: str | None = None
  address: Address | None = None


def contact_serializer( contact ) -> dict:
	return {
		"id": str( contact.get('_id')),
		"cpf": contact.get('cpf'),
		"company_name": contact.get('company_name'),
		"trade_name": contact.get('trade_name'),
		"email": contact.get('email'),
		"phone": contact.get('phone'),
		"contact_type": contact.get('contact_type'),
		"address": contact.get('address')
	}