from pydantic import BaseModel # type: ignore


class PatologiResponse(BaseModel):
    id: int
    nama: str
    
    class Config:
        orm_mode = True 

class PatologiDetailResponse(BaseModel):
    nama: str
    foto: str
    deskripsi: str
    createdAt: str
    updatedAt: str
    
    class Config:
        orm_mode = True 