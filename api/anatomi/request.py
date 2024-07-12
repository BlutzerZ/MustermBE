from datetime import date
from pydantic import BaseModel # type: ignore


class AnatomiRequest(BaseModel):
    nama: str
    foto: str
    deskripsi: str
    
    class Config:
        orm_mode = True 