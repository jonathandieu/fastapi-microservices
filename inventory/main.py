from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORDSMiddleware

app = FastAPI()

class Product(HashModel):
    name: str
    price: float
    quantity: int

@app.get("/")
async def root():
    return {"message" : "testing!"}

@app.get("/products")
def all():
    return Product.all_pks()
