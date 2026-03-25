import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models.unidade import Unidade
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
]

print(df.head())

with app.app_context():
    unidade = db.session.execute(select(Unidade).where(Unidade.nome == "CHU")).scalar_one_or_none()
    print(unidade)