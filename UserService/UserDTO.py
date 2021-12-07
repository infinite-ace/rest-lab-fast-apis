from pydantic import BaseModel


class UserDTO(BaseModel):
    id: str
    name: str
    age: int
    address: str
