from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.models.entity import Entity

class Evento(Entity):
    nome = Column(String, index=True, nullable=False)
    local = Column(String, index=True, nullable=False)
    descricao = Column(String, default="")
    data_hora = Column(DateTime, default=datetime.now)
    inscritos = Column(Integer, default=0)
    aberto = Column(Boolean, default=False)
