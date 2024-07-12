from fastapi import FastAPI # type: ignore
from config import database
from api.patologi.routes import router as patologi_router
from api.terminologi.routes import router as terminologi_router

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(patologi_router)
app.include_router(terminologi_router)