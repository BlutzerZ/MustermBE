from typing import Union

from sqlalchemy import or_
from config import database
from api.anatomi import models, response, request
from fastapi import APIRouter

router = APIRouter()

@router.get("/anatomi", response_model=list[response.AnatomiResponse], tags=["Anatomi"])
async def get_all_anatomi(
        page: Union[int, None] = None,
        limit: Union[int, None] = None,
    ):
    db = database.SessionLocal()
    
    if page == None:
        anatomis = db.query(models.Anatomi).limit(100 if limit == None else limit).all()
    else:
        offset = (page - 1) * limit
        anatomis = db.query(models.Anatomi).offset(offset).limit(limit).all()

    db.close()
    return anatomis


@router.get("/anatomi/{anatomi_id}", response_model=response.AnatomiDetailResponse, tags=["Anatomi"])
async def get_by_id_anatomi(
        anatomi_id: int,
    ):
    db = database.SessionLocal()

    anatomi = db.query(models.Anatomi).filter_by(id=anatomi_id).first()
    
    db.close()
    return anatomi


@router.post("/anatomi", response_model=response.AnatomiDetailResponse, tags=["Anatomi"])
async def insert_anatomi(
        anatomi_data: request.AnatomiRequest,
    ):
    db = database.SessionLocal()
    
    try:
        new_anatomi = models.Anatomi(
            nama=anatomi_data.nama, 
            foto=anatomi_data.foto, 
            deskripsi=anatomi_data.deskripsi,
        )
        db.add(new_anatomi)
        db.commit()
        db.refresh(new_anatomi)
        return new_anatomi
    except:
        db.rollback()
        raise
    finally:
        db.close()


@router.put("/anatomi/{anatomi_id}", response_model=response.AnatomiDetailResponse, tags=["Anatomi"])
async def update_anatomi(
        anatomi_data: request.AnatomiRequest,
        anatomi_id: int,
    ):
    db = database.SessionLocal()

    anatomi = db.query(models.Anatomi).filter(models.Anatomi.id == anatomi_id).first()
    if not anatomi:
        return None
    try:
        anatomi.nama = anatomi_data.nama
        anatomi.foto = anatomi_data.foto
        anatomi.deskripsi = anatomi_data.deskripsi
        db.commit()
        db.refresh(anatomi)
        return anatomi
    except:
        db.rollback()
        raise
    finally:
        db.close()
    
@router.delete("/anatomi/{anatomi_id}", tags=["Anatomi"])
async def update_anatomi(
        anatomi_id: int,
    ):
    db = database.SessionLocal()

    anatomi = db.query(models.Anatomi).filter(models.Anatomi.id == anatomi_id).first()
    if not anatomi:
        raise
    try:
        db.delete(anatomi)
        db.commit()
        return {"message": f"id {anatomi_id} success deleted"}
    except:
        db.rollback()
        raise
    finally:
        db.close()
    

@router.get("/search/anatomi", response_model=list[response.AnatomiResponse], tags=["Anatomi"])
async def search_anatomii(
        q: str,
    ):
    db = database.SessionLocal()

    anatomis = db.query(models.Anatomi).filter(or_(models.Anatomi.nama.ilike(f"%{q}%"), models.Anatomi.deskripsi.ilike(f"%{q}%"))).all()
    
    db.close()
    return anatomis
