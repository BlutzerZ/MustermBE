from pydantic import BaseModel # type: ignore


class TerminologiRequest(BaseModel):
    nama: str
    arti: str
    kategori: str
    
    class Config:
        orm_mode = True 