# %%
# jupyter cause why not

import pandas as pd

melbourne = "melb_data.csv"

melbourne_data = pd.read_csv(melbourne)

# info -> print
melbourne_data.describe()

# %%
