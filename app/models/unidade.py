from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app import db

if TYPE_CHECKING:
    from app.models.demanda import Demanda

class Unidade(db.Model):
    __tablename__ = "unidades"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True)

    demandas: Mapped[List["Demanda"]] = relationship(back_populates="unidade")

    def __repr__(self) -> str:
        return f"<Unidade {self.nome}>"