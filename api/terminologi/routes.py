from config import database
from api.terminologi import models, response
from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/terminologi", response_model=list[response.TerminologiResponse])
async def get_paged_terminologi(
        cat: Union[str, None] = None, 
        page: Union[int, None] = None,
        limit: Union[int, None] = None,
    ):
    db = database.SessionLocal()

    if page == None:
        if cat == None:
            terminologis = db.query(models.Terminologi).limit(100 if limit == None else limit).all()
        else:
            terminologis = db.query(models.Terminologi).filter_by(kategori=cat).limit(100 if limit == None else limit).all()
        return terminologis

    else:    
        offset = (page - 1) * limit
        if cat == None:
            terminologis = db.query(models.Terminologi).offset(offset).limit(limit).all()
        else:
            terminologis = db.query(models.Terminologi).filter_by(kategori=cat).offset(offset).limit(limit).all()
        return terminologis

@router.get("/terminologi/{terminologi_id}", response_model=response.TerminologiDetailsResponse)
async def get_by_id_terminologi(
        terminologi_id: int,
    ):
    db = database.SessionLocal()
    terminologi = db.query(models.Terminologi).filter_by(id=terminologi_id).first()
    return terminologi


@router.get("/search/terminologi", response_model=list[response.TerminologiResponse])
async def get_by_id_terminologi(
        q: str,
    ):
    db = database.SessionLocal()
    terminologis = db.query(models.Terminologi).filter(models.Terminologi.nama.ilike(q)).all()
    return terminologis
