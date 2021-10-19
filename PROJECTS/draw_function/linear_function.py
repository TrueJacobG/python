import numpy as np
import matplotlib.pyplot as plt


def drawLineFunc(a: float, b: float, start: float = -5, end: float = -5):
    x = np.array(np.arange(start, end+1))
    y = a * x + b
    plt.plot(x, y)
    plt.show()
