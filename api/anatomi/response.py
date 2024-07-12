from datetime import date
from pydantic import BaseModel # type: ignore


class AnatomiResponse(BaseModel):
    id: int
    nama: str
    deskripsi: str
    
    class Config:
        orm_mode = True 

class AnatomiDetailResponse(BaseModel):
    nama: str
    foto: str
    deskripsi: str
    createdAt: date
    updatedAt: date
    
    class Config:
        orm_mode = True 