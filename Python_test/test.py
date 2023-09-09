# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

xmin, xmax = -np.pi, np.pi
x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.plot(x, y_tan)
plt.hlines([-1, 1], xmin, xmax, linestyles="dashed")
plt.title(r"sin(x) and cos(x) and tan(x)")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

print('グラフ表示')
plt.show()
