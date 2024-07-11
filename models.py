from sqlalchemy import Column, Integer, String, Text, DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime

Base = declarative_base()

class Patologi(Base):
    __tablename__ = 'patologi'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    foto = Column(String(255))
    deskripsi = Column(Text)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Terminologi(Base):
    __tablename__ = 'terminologi'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    arti = Column(Text, nullable=False)
    kategori = Column(String(255))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
