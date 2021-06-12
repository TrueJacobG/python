# %%

# jupyter cause why not
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

melbourne = "melb_data.csv"
melbourne_data = pd.read_csv(melbourne)
# info -> print
melbourne_data.describe()

# %%

melbourne_data.columns
# %%

# remove
melbourne_data.dropna(axis=0)

# %%

y = melbourne_data.Price

# features -> things that you will use to make predictions
melbourne_features = ['Rooms', 'Bathroom',
                      'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
X.describe()
X.head()
# %%

# create a model
melbourne_model = DecisionTreeRegressor(random_state=1)

# fit a model
melbourne_model.fit(X, y)

# %%

# print prediction
print(X.head())
print(melbourne_model.predict(X.head()))

# %%
