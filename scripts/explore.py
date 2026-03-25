import pandas as pd

df = pd.read_excel("data/Planilha Processos Gerais - Folha 01, 02 e 03.2025.xlsx", sheet_name="Folha 01.25", header=1)

print("Colunas encontradas:")
for col in df.columns:
    print(repr(col))

print("\n Primeiras 3 linhas:")
print(df.head(3))