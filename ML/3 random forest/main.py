# %%

from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

path = "../melb_data.csv"
data = pd.read_csv(path)

y = data.Price
features = ['Rooms', 'Bathroom',
            'Landsize', 'Lattitude', 'Longtitude']
X = data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y)


# %%

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(
        max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    return mean_absolute_error(val_y, predictions)


leaves = []
means = []

for max_leaf_nodes in [x for x in range(300, 2000)]:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)

    leaves.append(max_leaf_nodes)
    means.append(mae)

plt.figure(0)
plt.plot(leaves, means)
plt.show()
# compare different max_leaf_nodes
# 866 the best

# %%

# random forest

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
forest_predictions = forest_model.predict(val_X)
print(mean_absolute_error(val_y, forest_predictions))

# much better than a single tree

# %%
