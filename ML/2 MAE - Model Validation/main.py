# %%


# error of predction -> error = |actual-predicted|


from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

path = "../melb_data.csv"
melbourne_data = pd.read_csv(path)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom',
                      'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)

# %%

# create abosolute error
predicted_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_prices))


# %%

# better validation data
# train data to make better prediction

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

melbourne_model = DecisionTreeRegressor(random_state=0)

melbourne_model.fit(train_X, train_y)

# create validation data
# to get better MAE

validated_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, validated_predictions))

# %%
