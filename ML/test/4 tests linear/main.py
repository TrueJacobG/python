
# %%
import tensorflow as tf
import numpy as np

# %%
model = tf.keras.Sequential([tf.keras.layers.Dense(units=10, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# y = 2x - 1
#x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
#y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

x = [float(x) for x in range(1, 51)]
y = [(2 * float(y)) - 1 for y in range(1, 51)]
x = np.array(x, dtype=float)
y = np.array(y, dtype=float)


# epochs - how many time we will test it
model.fit(x, y, epochs=1000)

# %%
m = np.amax(model.predict([5.0]))
print(int(m))

# %%
