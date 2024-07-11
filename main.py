from fastapi import FastAPI # type: ignore
import response
from config import database
import models

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


@app.get("/patologi/", response_model=list[response.PatologiResponse])
def get_all_patologi():
    db = database.SessionLocal()
    patologis = db.query(models.Patologi).all()
    return patologis