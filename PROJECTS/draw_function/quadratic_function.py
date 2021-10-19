import numpy as np
import matplotlib.pyplot as plt


def drawQuadFunc(a: float, b: float, c: float, start: float = -5, end: float = 5):
    x = np.array(np.arange(start, end+1))
    y = a * x * x + b * x + c
    plt.plot(x, y)
    plt.show()
