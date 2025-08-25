# %%
import numpy as np

mtz = np.arange(1, 10, 1).reshape(3, 3)

print(mtz)

# %%
print(mtz > 5)
print(mtz[mtz > 5])

# %%
print(mtz[mtz%2==0])