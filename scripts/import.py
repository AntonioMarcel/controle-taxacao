import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models.acao import Acao
from app.models.demanda import Demanda
from app.models.taxador import Taxador
from app.models.unidade import Unidade
from datetime import date
import pandas as pd
from sqlalchemy import select

app = create_app()

df = pd.read_excel("data/Planilha Processos Gerais - Folha 01, 02 e 03.2025.xlsx", sheet_name="Folha 01.25", header=1)

colunas_necessarias = [
    "PROCESSO SEI",
    "QUANTIDADE MASP\n(Quantidade de demandas enviadas no processo SEI em questão)",
    "UNIDADE\n(Lista suspensa)",
    "AÇÃO (ASSUNTO SEI)\n(Lista suspensa)",
    "ENTRADA NA CCPT\n(Data de recebimento do processo)",
    "QUANTIDADE TAXADOS",
    "TAXADOR RESPONSÁVEL\n(Lista suspensa)",
    "OBSERVAÇÕES",
]

df = df[colunas_necessarias]
df.columns = [
    "processo_sei",
    "quantidade_masp",
    "unidade",
    "acao",
    "entrada_ccpt",
    "quantidade_taxados",
    "taxador",
    "observacoes",
]

print(df)

# Remove espaços em branco nas seguintes colunas
df["acao"] = df["acao"].str.strip()
df["unidade"] = df["unidade"].str.strip()
df["taxador"] = df["taxador"].str.strip()

# Trata erros de inserção dos dados
df["acao"] = df["acao"].str.replace("FREQUENCIA", "FREQUÊNCIA")
df["acao"] = df["acao"].str.replace("ALTERAÇÃO DE DADOS BANCARIOS", "ALTERAÇÃO DE DADOS BANCÁRIOS")

with app.app_context():

    demandas = []

    for _, row in df.iterrows():

        # Busca os registros pelos nomes
        unidade = db.session.execute(select(Unidade).where(Unidade.nome == row["unidade"])).scalar_one_or_none()
        acao = db.session.execute(select(Acao).where(Acao.nome == row["acao"])).scalar_one_or_none()
        taxador = db.session.execute(select(Taxador).where(Taxador.nome == row["taxador"])).scalar_one_or_none()

        # Proteger quando registro for vazio 
        unidade_id = unidade.id if unidade else None
        acao_id = acao.id if acao else None
        taxador_id = taxador.id if taxador else None

        # Convert NaN values to None
        quantidade_taxados = None if pd.isna(row["quantidade_taxados"]) else int(row["quantidade_taxados"])
        observacoes = None if pd.isna(row["observacoes"]) else row["observacoes"]

        demanda = Demanda(
            processo_sei=row["processo_sei"],
            quantidade_masp=int(row["quantidade_masp"]),
            competencia=date(2025, 1, 1),
            unidade_id=unidade_id,
            acao_id=acao_id,
            entrada_ccpt=row["entrada_ccpt"],
            quantidade_taxados= quantidade_taxados,
            taxador_id=taxador_id,
            observacoes=observacoes,
        )

        demandas.append(demanda)

    db.session.add_all(demandas)
    db.session.commit()
