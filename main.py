from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from sqlalchemy import text

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/test-db/")
async def test_database(db: AsyncSession = Depends(get_db)):
    try:
        # Проверяем соединение, отправляя простой запрос
        await db.execute(text('SELECT 1'))
        return {"status": "Connected to the database!"}
    except Exception as e:
        return {"status": "Failed to connect to the database", "error": str(e)}