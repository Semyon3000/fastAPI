from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
import crud

app = FastAPI()

# Создание таблиц
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/items/")
async def create_item(name: str, description: str, price: int, quantity: int, db: AsyncSession = Depends(get_db)):
    return await crud.create_item(db, name, description, price, quantity)

@app.get("/items/")
async def read_items(db: AsyncSession = Depends(get_db)):
    return await crud.get_items(db)

@app.get("/items/{item_id}")
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await crud.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, description: str, price: int, quantity: int, db: AsyncSession = Depends(get_db)):
    item = await crud.update_item(db, item_id, name, description, price, quantity)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}