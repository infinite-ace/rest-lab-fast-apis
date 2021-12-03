from pydantic import BaseModel


class UserDTO(BaseModel):
    name: str
    age: int
    address: str
