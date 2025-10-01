# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("paises.csv", sep=';')
dfMaioresGDP = df.nlargest(5, 'GDP ($ per capita)')

# %%
plt.bar(dfMaioresGDP["Country"], dfMaioresGDP['GDP ($ per capita)'])

# %%
dfNoCoast = df[df['Coastline (coast/area ratio)'] == 0]
dfNoCoast

# %%
plt.pie([len(dfNoCoast), len(df)-len(dfNoCoast)], autopct="%1.1f%%", labels=["Paises sem  costa", "Paises com costas"])