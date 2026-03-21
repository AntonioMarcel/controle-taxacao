from datetime import date
from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, String, Text
from app import db

if TYPE_CHECKING:
    from app.models.acao import Acao
    from app.models.taxador import Taxador
    from app.models.unidade import Unidade

class Demanda(db.Model):
    __tablename__ = "demandas"

    id: Mapped[int] = mapped_column(primary_key=True)
    processo_sei: Mapped[str] = mapped_column(String(100))
    quantidade_masp: Mapped[int] = mapped_column()
    competencia: Mapped[date] = mapped_column(Date)
    unidade_id: Mapped[int] = mapped_column(ForeignKey("unidades.id"))
    acao_id: Mapped[int] = mapped_column(ForeignKey("acoes.id"))
    entrada_ccpt: Mapped[date] = mapped_column(Date)
    quantidade_taxados: Mapped[Optional[int]] = mapped_column(nullable=True)
    taxador_id: Mapped[Optional[int]] = mapped_column(ForeignKey("taxadores.id"), nullable=True)
    observacoes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relacionamentos
    unidade: Mapped["Unidade"] = relationship(back_populates="demandas") 
    acao: Mapped["Acao"] = relationship(back_populates="demandas") 
    taxador: Mapped["Taxador"] = relationship(back_populates="demandas") 

    def __repr__(self) -> str:
        return f"<Demanda {self.id} - {self.processo_sei}>"