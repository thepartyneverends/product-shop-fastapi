from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

from app.database import engine

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    quantity = Column(Integer)
    rating = Column(Float)
    dealer = Column(String)


Base.metadata.create_all(engine)
