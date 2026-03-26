from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app import db

if TYPE_CHECKING:
    from app.models.demanda import Demanda

class Acao(db.Model):
    __tablename__ = "acoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True)

    demandas: Mapped[List["Demanda"]] = relationship(back_populates="acao")

    def __repr__(self) -> str:
        return f"<Acao {self.id} - {self.nome}>"