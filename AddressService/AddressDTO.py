from pydantic import BaseModel


class AddressDTO(BaseModel):
    user_id: str
    address: str
