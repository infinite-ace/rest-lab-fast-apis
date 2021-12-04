import uvicorn
from fastapi import FastAPI

app = FastAPI()

address_dict = {}


@app.get("/")
async def root():
    return {"message": "Hello Address Service"}


@app.post('/address')
def set_address(id: str, address: str):
    address_dict[id] = address
    return address_dict

@app.get('/all')
def all():
    return address_dict


if __name__ == "__main__":
    uvicorn.run("address_service:app", host="127.0.0.1", port=8001)
