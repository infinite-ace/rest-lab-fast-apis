import requests
import uvicorn
from fastapi import FastAPI

from AddressDTO import AddressDTO

app = FastAPI()

address_dict = {}


@app.get("/")
async def root():
    return {"message": "Hello Address Service"}


@app.post('/create')
def set_address(id: str, address: str):
    address_dict[id] = address
    return address_dict


@app.get('/read')
def get_address(user_id: str):
    return address_dict[user_id]


@app.put('/update')
def update_address(address: AddressDTO):
    address_dict[address.user_id] = address.address

@app.delete('/delete')
def delete_address(address: AddressDTO):
    address_dict.pop(address.user_id)


@app.get('/all')
def all():
    return address_dict


if __name__ == "__main__":
    uvicorn.run("address_service:app", host="127.0.0.1", port=8001)
