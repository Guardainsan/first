from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
items = {}


@app.put("/items/{item_id}")
async def update_item(item_id: int):
    if item_id in items:
        items[item_id] = {"name"}
        return items[item_id]
    return {"error": "Item not found"}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    else:
        return {"error": "Item not found"}


@app.post("/items/{item_id}")
async def create_item(item_id: int, name: str, description: str):
    if item_id in items:
        return {"error": "Item already exists"}
    items[item_id] = {"name": name, "description": description}
    return items[item_id]