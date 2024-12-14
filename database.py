from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:tar1234563@localhost/postgres"

# Создание движка SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Сессии для взаимодействия с базой
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Функция получения сессии
async def get_db():
    async with async_session() as session:
        yield session