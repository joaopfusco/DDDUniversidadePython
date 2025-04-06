from datetime import datetime
from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema

class EventoIn(BaseModel):
    nome: str
    local: str
    descricao: str
    data_hora: datetime
    inscritos: int
    aberto: bool

class EventoOut(EntitySchema, EventoIn):
    pass