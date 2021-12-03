import uvicorn
from fastapi import Request, FastAPI

from UserDTO import UserDTO

app = FastAPI()

users_dictionary = {}


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
async def create_user(user: UserDTO):

    users_dictionary[user.id] = user
    return user


@app.delete("/delete")
def delete_user(request: Request):
    request_body = request.json()

    user = UserDTO.create(
        request_body['id'],
        request_body['name'],
        request_body['age'],
        request_body['address']
    )

    users_dictionary.remove(user)
    return users_dictionary


@app.get("/getall")
async def get_all_users():
    return users_dictionary


@app.get("/")
def root():
    return {"message": "Hello Users Service"}


if __name__ == "__main__":
    uvicorn.run("users_service:app", host="127.0.0.1", port=8000)
