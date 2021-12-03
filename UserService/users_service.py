import uvicorn
from fastapi import Request, FastAPI

from User import User

app = FastAPI()

users_dictionary = []


@app.get("/")
async def root():
    return {"message": "Hello Users Service"}


@app.post("/create")
async def create_user(request: Request):
    request_body = await request.json()

    user = User(request_body['name'],
                request_body['age'],
                request_body['address'])

    users_dictionary.append(user)
    return users_dictionary


@app.get("/getall")
async def get_all_users():
    return users_dictionary


if __name__ == "__main__":
    uvicorn.run("users_service:app", host="127.0.0.1", port=8000)
