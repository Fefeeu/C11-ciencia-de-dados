# %%
import pandas as pd

df = pd.read_csv("C:\Users\felip\OneDrive\Desktop\estudos\Docs Inatel\C11 - Ciencia de Dados\Repositorio GitHub\Aulas\aula_05\paises.csv", sep=";")

df['Porcentagem Pop. paiz/mundo'] = (df["Population"] / df["Population"].sum()) * 100

df.to_csv("paises_com_porcentagem.csv")
print(df)

# %%
group_regiao = df.groupby("Region")
print(group_regiao["Country"].count())

# %% 10% de desconto
def tenpercent(x: float) -> float:
    return x * 0.90

taxaMort = df["Deathrate"]
taxaMortDesconto = taxaMort.apply(tenpercent)

df2 = pd.concat([taxaMort, taxaMortDesconto], axis=1)
df2.columns = ["taxa mortalidade", "taxa mortalidade com desconto"]
print(df2)

# %%
df.dropna()