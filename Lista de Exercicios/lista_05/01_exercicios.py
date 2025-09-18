# %%
import pandas as pd

df = pd.read_csv("paises.csv", sep=';')

# %% EXERCICIO 1
df["Region"] = df["Region"].str.strip()
paises_oceania = df[df["Region"] == "OCEANIA"]["Country"]

quantidade_paises_oceania = df.groupby("Region").count()["Country"]["OCEANIA"]

print(f"A OCEANIA possui {quantidade_paises_oceania} paies, sendo eles:\n", paises_oceania)

# %% EXERCICIO 2
pais_mais_povoado = df.iloc[df["Population"].argmax()][["Country", "Region"]]
print(f"{pais_mais_povoado["Country"]} é o pais com maior populacao, ficando na regiao: {pais_mais_povoado["Region"]}")

# %% EXERCICIO 3
media_alfabetizacao = df[["Region", "Literacy (%)"]].groupby("Region")
print("Media de alfabetização das regioes:\n", media_alfabetizacao["Literacy (%)"].mean())

# %% EXERCICIO 4
paises_sem_costa = df[df["Coastline (coast/area ratio)"] == 0]
paises_sem_costa.reset_index().to_csv("noCoast.csv")

# %% EXERCICIO 5
def categoria_taxa_mortalidade(Deathrate: float)->str:
    if(Deathrate < 9):
        return "Balanced"
    else:
        return "Urgent"

df["Humanitarian Help"] = df["Deathrate"].apply(categoria_taxa_mortalidade)
print(df)
# %%
