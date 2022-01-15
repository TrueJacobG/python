# %%
import tensorflow as tf
import pandas as pd


# %%
dataframe = pd.read_excel("data.xlsx", usecols="A:B")

sizes = dataframe["HouseSize"].to_numpy()
prices = dataframe["Price"].to_numpy()

# %%
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer="sgd", loss=tf.keras.losses.MeanAbsoluteError())

# %%
when_stop = tf.keras.callbacks.EarlyStopping(
    monitor="loss", mode="min", patience=5)

# patience - how many echos it should do try after reaching the halt

# verbose = 0 - disable verbose logging

model.fit(sizes, prices, epochs=10000, verbose=0, callbacks=when_stop)


# %%
print(model.predict([300]))

# %%
