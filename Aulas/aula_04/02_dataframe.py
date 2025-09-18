# %%
import pandas as pd
import numpy as np

df = pd.DataFrame(index=["A","B","C","D","E"],
                  columns=["W","X","Y","Z"],
                  data=np.random.randint(1, 50, [5,4]))
print(df)

# %%
print(df.iloc[0:2, :])

# %%
print(df.loc[["A","B"], ["W", "Y"]])

# %%
print(df[["W", "Y"]])