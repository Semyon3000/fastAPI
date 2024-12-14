from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Item

# Создать запись
async def create_item(db: AsyncSession, name: str, description: str, price: int, quantity: int):
    new_item = Item(name=name, description=description, price=price, quantity=quantity)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

# Прочитать данные
async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()

async def get_item_by_id(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()

# Обновить запись
async def update_item(db: AsyncSession, item_id: int, name: str, description: str, price: int, quantity: int):
    item = await get_item_by_id(db, item_id)
    if item:
        item.name = name
        item.description = description
        item.price = price
        item.quantity = quantity
        await db.commit()
        return item
    return None

# Удалить запись
async def delete_item(db: AsyncSession, item_id: int):
    item = await get_item_by_id(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()
        return True
    return False