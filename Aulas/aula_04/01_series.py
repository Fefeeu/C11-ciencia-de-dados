# %%
import pandas as pd

indices = ['a', 'b', 'c']
valores = [1, 2, 3]

serie = pd.Series(index=indices, data=valores)
print(serie)
print(type(serie))

# %%
dic1 = {'a':10, 'b':20, 'c':30}
dic2 = {'a':10, 'b':20, 'd':40}

serie1 = pd.Series(dic1)
serie2 = pd.Series(dic2)

print(serie1 + serie2)

# %%
print(serie1 - serie2)

serie.notnull()

# %%
print(serie1.add(serie2, fill_value=0))
print(serie1.sub(serie2, fill_value=0))