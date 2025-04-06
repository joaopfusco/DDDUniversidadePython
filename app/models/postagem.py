from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.entity import Entity

class Postagem(Entity):
    autor_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    autor = relationship("Usuario", backref="postagens")
    
    conteudo = Column(String, default="")
    data_hora = Column(DateTime, default=datetime.now)
    curtidas = Column(Integer, default=0)
    comentarios = Column(Integer, default=0)
