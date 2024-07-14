from typing import Union

from sqlalchemy import or_
from config import database
from api.patologi import models, response, request
from fastapi import APIRouter

router = APIRouter()

@router.get("/patologi", response_model=list[response.PatologiResponse], tags=["Patologi"])
async def get_all_patologi(
        page: Union[int, None] = None,
        limit: Union[int, None] = None,
    ):
    db = database.SessionLocal()
    
    if page == None:
        patologis = db.query(models.Patologi).limit(100 if limit == None else limit).all()
    else:
        offset = (page - 1) * limit
        patologis = db.query(models.Patologi).offset(offset).limit(limit).all()
        
    db.close()
    return patologis


@router.get("/patologi/{patologi_id}", response_model=response.PatologiDetailResponse, tags=["Patologi"])
async def get_by_id_patologi(
        patologi_id: int,
    ):
    db = database.SessionLocal()

    patologi = db.query(models.Patologi).filter_by(id=patologi_id).first()
    
    db.close()
    return patologi


@router.post("/patologi", response_model=response.PatologiDetailResponse, tags=["Patologi"])
async def insert_patologi(
        patologi_data: request.PatologiRequest,
    ):
    db = database.SessionLocal()
    
    try:
        new_patologi = models.Patologi(
            nama=patologi_data.nama, 
            foto=patologi_data.foto, 
            deskripsi=patologi_data.deskripsi,
        )
        db.add(new_patologi)
        db.commit()
        db.refresh(new_patologi)
        return new_patologi
    except:
        db.rollback()
        raise
    finally:
        db.close()


@router.put("/patologi/{patologi_id}", response_model=response.PatologiDetailResponse, tags=["Patologi"])
async def update_patologi(
        patologi_data: request.PatologiRequest,
        patologi_id: int,
    ):
    db = database.SessionLocal()

    patologi = db.query(models.Patologi).filter(models.Patologi.id == patologi_id).first()
    if not patologi:
        return None
    try:
        patologi.nama = patologi_data.nama
        patologi.foto = patologi_data.foto
        patologi.deskripsi = patologi_data.deskripsi
        db.commit()
        db.refresh(patologi)
        return patologi
    except:
        db.rollback()
        raise
    finally:
        db.close()
    
@router.delete("/patologi/{patologi_id}", tags=["Patologi"])
async def update_patologi(
        patologi_id: int,
    ):
    db = database.SessionLocal()

    patologi = db.query(models.Patologi).filter(models.Patologi.id == patologi_id).first()
    if not patologi:
        raise
    try:
        db.delete(patologi)
        db.commit()
        return {"message": f"id {patologi_id} success deleted"}
    except:
        db.rollback()
        raise
    finally:
        db.close()
    

@router.get("/search/patologi", response_model=list[response.PatologiResponse], tags=["Patologi"])
async def search_patologii(
        q: str,
    ):
    db = database.SessionLocal()

    patologis = db.query(models.Patologi).filter(or_(models.Patologi.nama.ilike(f"%{q}%"), models.Patologi.deskripsi.ilike(f"%{q}%"))).all()
    
    db.close()
    return patologis
