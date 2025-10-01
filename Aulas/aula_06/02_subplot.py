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

plt.subplot(1,2,1)
plt.plot(x, y, ":o", color="red")

plt.subplot(1,2,2)
plt.plot(x, y2, "-s", color="blue")

plt.show()