from sqlalchemy import Column, Integer, String, Text, Date # type: ignore
from datetime import date
from config.database import Base

class Patologi(Base):
    __tablename__ = 'patologi'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    foto = Column(String(255))
    deskripsi = Column(Text)
    createdAt = Column(Date, default=date.today())
    updatedAt = Column(Date, default=date.today(), onupdate=date.today())