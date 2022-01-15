# %%
import numpy as np
import tensorflow as tf

# %%
x = np.arange(-3, 4, 1)
y = np.array([-6, -4, -2, 0, 2, 4, 6])


model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer="sgd", loss="mean_absolute_error")

model.fit(x, y, epochs=500)

# %%
print(model.predict([11]))

# %%
