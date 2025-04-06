from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import create_tables
from app.routers.usuario_router import usuario_router
from app.routers.seguidor_router import seguidor_router
from app.routers.evento_router import evento_router
from app.routers.postagem_router import postagem_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(usuario_router)
app.include_router(seguidor_router)
app.include_router(evento_router)
app.include_router(postagem_router)
