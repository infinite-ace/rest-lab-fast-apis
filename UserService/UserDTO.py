

class UserDTO:
    id: int
    name: str
    age: int
    address: str

    def __init__(self,id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def create(id, name, age, address):
        user = UserDTO()
        user.id = id
        user.name = name
        user.age = age
        user.address = address

        return user
