class User:
    name = ""
    age = 0
    favourite_book = ""
    address = ""

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def create(name, age, address):
        user = User()
        user.name = name
        user.age = age
        user.address = address

        return user
