from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def home():
    return {"Data": "T"}


class Item(BaseModel):
    name: str
    amount: int
    price: int


shop = {
    1: {
        "name": "Chocolate",
        "amount": 10,
        "price": 8
    }
}


@app.get('/shop-list/')
def shop_list():
    return shop


@app.get('/shop/{item_id}')
def get_item_by_item_id(item_id: int = Path(None, description="Nice item :D")):
    # description will be in the localhost/docs
    return shop[item_id]


@app.get('/shop-item/')
def get_item_by_name(*, name: Optional[str] = None):
    # localhost/shop?name=Chocolate
    for i in shop:
        if shop[i]["name"] == name:
            return shop[i]
    return {"Data": name + " not found."}


@app.post("/shop/create/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in shop:
        return {"Error": "Item already exists!"}
    shop[item_id] = item


@app.put("/shop/update/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in shop:
        return {"Error": "Item not found."}
    shop[item_id] = item
    return shop[item_id]
