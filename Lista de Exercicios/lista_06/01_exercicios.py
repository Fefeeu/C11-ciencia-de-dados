# %%
"""
!!!!!!!!!!!!!!!!!!!!
PARA ESSE CODIGO FUNCIONAR, PRECISA RODAR O CODIGO TODO DE UMA VEZ
PARA MOSTRAR TODOS OS GRAFICOS JUNTOS
!!!!!!!!!!!!!!!!!!!!
"""
import pandas as pd
import matplotlib.pyplot as plt

df_paises = pd.read_csv("paises.csv", sep=';')
df_espaco = pd.read_csv("space.csv", sep=';')

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 6))

# %% EXERCICIO 1
df_paises_norte_america = df_paises[df_paises['Region'].str.contains("NORTHERN AMERICA")]
ax1.set_title('Mortalidade Vs Natalidade')
ax1.grid(True)
ax1.plot(df_paises_norte_america['Country'], df_paises_norte_america['Deathrate'], '-o', color='red')
ax1.plot(df_paises_norte_america['Country'], df_paises_norte_america['Birthrate'], '-o', color='green')
ax1.legend(["Mortalidade", "Natalidade"])
ax1.tick_params(axis='x', rotation=45)

# %% EXERCICIO 2
empresas_eua = df_espaco[df_espaco['Location'].str.contains('USA')]['Company Name']
empresas_unicas_eua = empresas_eua.unique()

empresas_china = df_espaco[df_espaco['Location'].str.contains('China')]['Company Name']
empresas_unicas_china = empresas_china.unique()

ax2.set_title("Quantidade de Empresas Únicas")
ax2.bar(["China", "EUA"], [len(empresas_unicas_china), len(empresas_unicas_eua)])

# %% EXERCICIO 3
df_missoes_roscosmos = df_espaco[df_espaco['Company Name'].str.contains('Roscosmos')]
roscosmos_status = df_missoes_roscosmos['Status Mission'].value_counts()
status = roscosmos_status.index

ax3.set_title('Status da Empresa Roscosmos')
ax3.pie(roscosmos_status,
        labels=status,
        autopct='%1.1f%%'
       )

# %%
plt.tight_layout()
plt.show()
