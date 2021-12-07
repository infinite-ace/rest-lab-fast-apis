import uvicorn
import requests
import uuid
from fastapi import Request, FastAPI

from UserDTO import UserDTO

app = FastAPI()

users_dictionary = {}
users_count = 0


#   Example:
#
  # {
  #   "id": 1,
  #   "name": "Zohan",
  #   "age": 332,
  #   "address": "12 Main Street, NY, 60049"
  # }
#
#


@app.post("/create")
def create_user(user: UserDTO):

    user_uuid = str(uuid.uuid4())
    address = user.address

    requests.post(f"http://127.0.0.1:8001/address?id={user_uuid}&address={address}").text

    users_dictionary[user_uuid] = user
    return user


@app.delete("/delete")
def delete_user(id: str):

    users_dictionary.pop(id, None)
    return users_dictionary


@app.get("/all")
async def get_all_users():
    print(users_count)
    return users_dictionary


@app.get("/")
def root():
    return {"message": "Hello Users Service"}


if __name__ == "__main__":
    uvicorn.run("users_service:app", host="127.0.0.1", port=8000)
