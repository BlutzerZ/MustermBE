from sqlalchemy import Column, Integer, String, Text, Date # type: ignore
from datetime import date
from config.database import Base

class Terminologi(Base):
    __tablename__ = 'terminologi'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    arti = Column(Text, nullable=False)
    kategori = Column(String(255))
    createdAt = Column(Date, default=date.today())
    updatedAt = Column(Date, default=date.today(), onupdate=date.today())
