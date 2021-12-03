import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Transaction Service"}

if __name__ == "__main__":
    uvicorn.run("transaction_service:app", host="127.0.0.1", port=8002)

