import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models.unidade import Unidade
from app.models.acao import Acao
from app.models.taxador import Taxador
from sqlalchemy import select 

app = create_app()

nomes_unidades = [
    "ADC",
    "CEPAI (ADC)",  # checar com gestão: mesmo que "CEPAI"?
    "CEPAI",        # checar com gestão: mesmo que "CEPAI (ADC)"?
    "CHB",
    "CHPB",         # checar com gestão: unidade válida?
    "CHE",
    "CHU",
    "CMT (ADC)",    # checar com gestão: mesmo que "CMT"?
    "CMT",          # checar com gestão: mesmo que "CMT (ADC)"?
    "CSPD",
    "CSSFA",
    "CSSFE",
    "CSSI",
    "HAC",
    "HBDS",         # checar com gestão: unidade válida?
    "HCM",
    "HEM",
    "HIJPII",
    "HJK",
    "HJXXIII",
    "HMAL",
    "HRAD (ADC)",   # checar com gestão: mesmo que "HRAD"?
    "HRAD",         # checar com gestão: mesmo que "HRAD (ADC)"?
    "HRBJA",
    "HRJP",
    "IRS",
    "MGT",          # checar com gestão: mesmo que "MGTX"?
    "MGTX",         # checar com gestão: mesmo que "MGT"?
    "MOV",
    "SEPLAG",
]

nomes_acoes = [
    "ABONO DE EMERGÊNCIA",
    "ABONO PERMANÊNCIA",
    "APOSTILA",
    "AD.NOT/FINAL DE SEMANA",
    "PMC",
    "ADICIONAL TRINTENÁRIO",
    "ADICIONAL DESEMPENHO",
    "AJUDA DE CUSTO",
    "ALTERAÇÃO DADOS CADASTRAIS",
    "ALTERAÇÃO DE DADOS BANCÁRIOS",
    "AFASTAMENTO PARA ESTUDOS",
    "ACERTOS DÉCIMO TERCEIRO",
    "ATUALIZAÇÃO PENSÃO",
    "AUXÍLIO/VALE TRANSPORTE",
    "ASSUNTOS PREVIDENCIÁRIOS",
    "APOSENTADORIA - EXCLUSÃO DE VERBAS",
    "CORREÇÃO IMPLANTAÇÃO",
    "CONTRACHEQUE",
    "COORDENAÇÃO CCPT",
    "DESLIGAMENTO",
    "DESLIGAMENTO DE NOMEADOS",
    "DOAÇÃO DE SANGUE",
    "EXONERAÇÃO",
    "QUINQUÊNIO/TRINTENÁRIO/PROMOÇÃO",
    "FGH",
    "FGTS - JUDICIAL",
    "FALTAS - DESCONTOS/RESTITUIÇÕES",
    "FÉRIAS PRÊMIO (INDENIZAÇÃO)",
    "FÉRIAS REGULAMENTARES (ACERTO)",
    "FREQUÊNCIA",
    "FREQUÊNCIA MENSAL",
    "GIEFS",
    "GRS",
    "HORA EXTRA",
    "HORA EXTRA MENSAL",
    "IMPLANTAÇÃO",
    "INÍCIO DE EXERCÍCIO",
    "INSS",
    "IPSEMG",
    "ISENÇÃO DE IR",
    "INCLUSÃO RESIDENTES",
    "INCLUSÃO ESTAGIÁRIOS",
    "INDENIZADO",
    "LICENÇA MATERNIDADE CONTRATO",
    "LIBERAÇÃO DE VERBAS RETIDAS",
    "MAPA JUDICIAL",
    "MOV. INTERNA",
    "NOMEAÇÃO DAI",
    "OPE",
    "ORIENTAÇÕES",
    "PAD",
    "PAGAMENTO DE DAE",
    "PAGAMENTO REJEITADO",
    "PENSÃO ALIMENTO",
    "PENSÃO BOLSISTA",
    "PISO ENFERMAGEM",
    "POSSE",
    "REMOÇÃO",
    "RENOVAÇÃO CONTRATO",
    "RENOVAÇÃO CONTRATO GESTANTE",
    "RENOVAÇÃO RESIDENTES",
    "RESUMO FUNCIONAL",
    "RETENÇÃO",
    "SISAP - SOLICITAÇÕES E SENHAS",
    "VENCIMENTOS DEIXADOS",
    "VERBAS RETIDAS",
    "VINCULADO",
]

nomes_taxadores = [
    "Jéssica",
    "Cleidson",
    "Giselle",
    "Liomar",
    "Paola",
    "Rhaissa",
    "Ingrid",
    "Fabiana",
    "Daniela",
    "Rosane",
    "Robô",
    "Ícaro",
    "Não identificado"
]

with app.app_context():

    def seed_nomes(nomes_data, model):
        stmt = select((model.nome))
        nomes_existentes = set(db.session.execute(stmt).scalars().all())    
        nomes_novos = [model(nome=nome) for nome in nomes_data if nome not in nomes_existentes] 
        db.session.add_all(nomes_novos)


    seed_nomes(nomes_unidades, Unidade)
    seed_nomes(nomes_acoes, Acao)
    seed_nomes(nomes_taxadores, Taxador)


    db.session.commit()


