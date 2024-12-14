from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = 'items'
    __table_args__ = {"schema": "IAD"}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Integer)
    quantity = Column(Integer)