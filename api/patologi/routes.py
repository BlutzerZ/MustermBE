from typing import Union
from config import database
from api.patologi import models, response
from fastapi import APIRouter

router = APIRouter()

@router.get("/patologi", response_model=list[response.PatologiResponse])
async def get_all_patologi(
        page: Union[int, None] = None,
        limit: Union[int, None] = None,
    ):
    if page == None:
        db = database.SessionLocal()
        patologis = db.query(models.Patologi).limit(100 if limit == None else limit).all()
    else:
        offset = (page - 1) * limit
        patologis = db.query(models.Patologi).offset(offset).limit(limit).all()

    return patologis

@router.get("/patologi/{patologi_id}", response_model=response.PatologiDetailResponse)
async def get_by_id_patologi(patologi_id: int):
    db = database.SessionLocal()
    patologi = db.query(models.Patologi).filter_by(id=patologi_id).first()
    return patologi

@router.get("/search/patologi", response_model=list[response.PatologiResponse])
async def search_patologii(
        q: str,
    ):
    db = database.SessionLocal()
    patologis = db.query(models.Patologi).filter(models.Patologi.nama.ilike(f"%{q}%")).all()
    return patologis
