from config import database
from api.terminologi import models, response, request
from fastapi import APIRouter
from typing import Union
from sqlalchemy import and_, or_

router = APIRouter()

@router.get("/terminologi", response_model=list[response.TerminologiResponse], tags=["Terminologi"])
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

    else:    
        offset = (page - 1) * limit
        if cat == None:
            terminologis = db.query(models.Terminologi).offset(offset).limit(limit).all()
        else:
            terminologis = db.query(models.Terminologi).filter_by(kategori=cat).offset(offset).limit(limit).all()
    
    db.close()
    return terminologis

@router.get("/terminologi/{terminologi_id}", response_model=response.TerminologiDetailsResponse, tags=["Terminologi"])
async def get_by_id_terminologi(
        terminologi_id: int,
    ):
    db = database.SessionLocal()
    terminologi = db.query(models.Terminologi).filter_by(id=terminologi_id).first()
    
    db.close()
    return terminologi

@router.post("/terminologi", response_model=response.TerminologiDetailsResponse, tags=["Terminologi"])
async def insert_terminologi(
        terminologi_data: request.TerminologiRequest,
    ):
    db = database.SessionLocal()

    try:
        terminologi = models.Terminologi(
            nama=terminologi_data.nama, 
            arti=terminologi_data.arti,
            kategori=terminologi_data.kategori,
        )
        db.add(terminologi)
        db.commit()
        db.refresh(terminologi)
        return terminologi
    except:
        db.rollback()
        raise
    finally:
        db.close()

@router.put("/terminologi/{terminologi_id}", response_model=response.TerminologiDetailsResponse, tags=["Terminologi"])
async def update_terminologi(
        terminologi_id: int,
        terminologi_data: request.TerminologiRequest,
    ):
    db = database.SessionLocal()

    terminologi = db.query(models.Terminologi).filter_by(id=terminologi_id).first()
    try:
        terminologi.nama=terminologi_data.nama, 
        terminologi.arti=terminologi_data.arti,
        terminologi.kategori=terminologi_data.kategori,
        db.commit()
        db.refresh(terminologi)
        return terminologi
    except:
        db.rollback()
        raise
    finally:
        db.close()


@router.delete("/terminologi/{terminologi_id}", tags=["Terminologi"])
async def delete_terminologi(
        terminologi_id: int,
    ):
    db = database.SessionLocal()

    terminologi = db.query(models.Terminologi).filter_by(id=terminologi_id).first()
    try:
        db.delete(terminologi)
        db.commit()
        return {"message": f"id {terminologi_id} success deleted"}
    except:
        db.rollback()
        raise
    finally:
        db.close()


@router.get("/search/terminologi", response_model=list[response.TerminologiResponse], tags=["Terminologi"])
async def get_by_id_terminologi(
        q: str,
        cat: str,
    ):
    db = database.SessionLocal()
    terminologis = db.query(models.Terminologi).filter(and_(
                                                            or_(
                                                                models.Terminologi.nama.ilike(f"%{q}%"), 
                                                                models.Terminologi.arti.ilike(f"%{q}%")
                                                            ), 
                                                            models.Terminologi.kategori == cat)
                                                       ).all()
    db.close()
    return terminologis
