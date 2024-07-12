from datetime import date
from pydantic import BaseModel # type: ignore


class TerminologiResponse(BaseModel):
    id: int
    nama: str
    arti: str
    
    class Config:
        orm_mode = True 

class TerminologiDetailsResponse(BaseModel):
    nama: str
    arti: str
    kategori: str
    createdAt: date
    updatedAt: date
    
    class Config:
        orm_mode = True 