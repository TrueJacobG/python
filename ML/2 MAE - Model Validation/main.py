# %%

# error of predction -> error = |actual-predicted|

from sklearn.model_selection import train_test_split
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


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

melbourne_model = DecisionTreeRegressor(random_state=0)

melbourne_model.fit(train_X, train_y)

# create validation data
# to get better MAE

validated_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, validated_predictions))

# %%

############################
# underfitting and overfitting
# how to make your model more accurate


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(
        max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    return mean_absolute_error(val_y, predictions)


for max_leaf_nodes in [10, 100, 500, 1000, 2000]:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {max_leaf_nodes} Mean Absolute Value: {mae}")

# the best deepness is 500
# the best number of leaves -> 500

# overfitting -> a lot of leaves, week with new data
# underfitting -> less accurate
# golden mean -> 😎😎😎
