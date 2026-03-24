from app import create_app, db
from app.models.unidade import Unidade
from app.models.acao import Acao
from app.models.taxador import Taxador
from sqlalchemy import select 

app = create_app()

nomes_unidades = [
    "ADC",
    "CEPAI (ADC)",
    "CHB",
    "HJXXIII",
    "CMT (ADC)",
    "CSPD",
    "CSSFA",
    "CSSFE",
    "CSSI",
    "HCM",
    "HEM",
    "HRAD (ADC)",
    "HRJP",
    "IRS",
    "HAC",
    "MGTX",
    "MOV",
    "HJK",
    "HIJPII",
    "HMAL",
    "CHU",
    "CHE",
    "SEPLAG",
    "HRBJA"
]

nomes_acoes = [
    "ABONO DE EMERGÊNCIA",
    "ABONO PERMANÊNCIA",
    "APOSTILA",
    "AD.NOT/FINAL DE SEMANA",
    "PMC",
    "ADICIONAL TRINTENÁRIO",
    "AJUDA DE CUSTO",
    "ALTERAÇÃO DADOS CADASTRAIS",
    "AUXÍLIO/VALE TRANSPORTE",
    "CORREÇÃO IMPLANTAÇÃO",
    "DESLIGAMENTO",
    "EXONERAÇÃO",
    "QUINQUÊNIO/TRINTENÁRIO/PROMOÇÃO",
    "FGH",
    "FALTAS - DESCONTOS/RESTITUIÇÕES",
    "FÉRIAS PRÊMIO (INDENIZAÇÃO)",
    "FÉRIAS REGULAMENTARES (ACERTO)",
    "FREQUÊNCIA",
    "FGTS - JUDICIAL",
    "GIEFS",
    "GRS",
    "HORA EXTRA",
    "IMPLANTAÇÃO",
    "INÍCIO DE EXERCÍCIO",
    "INSS",
    "IPSEMG",
    "ISENÇÃO DE IR",
    "LICENÇA MATERNIDADE CONTRATO",
    "MAPA JUDICIAL",
    "MOV. INTERNA",
    "NOMEAÇÃO DAI",
    "PAD",
    "PENSÃO ALIMENTO",
    "PENSÃO BOLSISTA",
    "POSSE",
    "REMOÇÃO",
    "RENOVAÇÃO CONTRATO",
    "RENOVAÇÃO RESIDENTES",
    "RESUMO FUNCIONAL",
    "RETENÇÃO",
    "VENCIMENTOS DEIXADOS",
    "VERBAS RETIDAS",
    "VINCULADO",
    "DESLIGAMENTO DE NOMEADOS",
    "OPE",
    "CONTRACHEQUE",
    "PISO ENFERMAGEM",
    "SISAP - SOLICITAÇÕES E SENHAS",
    "ASSUNTOS PREVIDENCIÁRIOS",
    "COORDENAÇÃO CCPT",
    "PAGAMENTO DE DAE",
    "APOSENTADORIA - EXCLUSÃO DE VERBAS",
    "AFASTAMENTO PARA ESTUDOS",
    "INCLUSÃO RESIDENTES",
    "ORIENTAÇÕES",
    "ACERTOS DÉCIMO TERCEIRO",
    "DOAÇÃO DE SANGUE",
    "ADICIONAL DESEMPENHO",
    "INCLUSÃO ESTAGIÁRIOS",
    "INDENIZADO",
    "RENOVAÇÃO CONTRATO GESTANTE",
    "ATUALIZAÇÃO PENSÃO"
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


