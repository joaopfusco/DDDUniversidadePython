from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema

class EventoIn(BaseModel):
    nome: str
    local: str
    descricao: str
    data_hora: str
    inscritos: int
    aberto: bool

class EventoOut(EntitySchema, EventoIn):
    pass