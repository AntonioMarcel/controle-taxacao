from typing import List, Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app import db

if TYPE_CHECKING:
    from app.models.demanda import Demanda

class Taxador(db.Model):
    __tablename__ = "taxadores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True)

    demandas: Mapped[List["Demanda"]] = relationship(back_populates="taxador")

    def __repr__(self) -> str:
        return f"<Taxador {self.id} - {self.nome}>"