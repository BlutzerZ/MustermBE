from datetime import date
from pydantic import BaseModel # type: ignore


class PatologiRequest(BaseModel):
    nama: str
    foto: str
    deskripsi: str
    
    class Config:
        orm_mode = True 