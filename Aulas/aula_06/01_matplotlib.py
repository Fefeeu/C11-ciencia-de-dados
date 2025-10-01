# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
x = np.array([1,2,3,4,5])
y = x ** 2
y2 = x ** 3
plt.xlabel("Valores X")
plt.ylabel("Valores Y")

plt.plot(x, y, ":o", color="red")
plt.plot(x, y2, "-s", color="blue")
plt.show()

# %%
df = pd.read_csv("paises.csv", sep=';')

maiores_paises = df.nlargest(6, "Area (sq. mi.)")

plt.scatter(maiores_paises["Country"], maiores_paises["Area (sq. mi.)"])
