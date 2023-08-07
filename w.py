import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100)
N = np.arange(-100, 100)
y = []
for i in N:
    for j in x:
        while len(y) != len(x):
            if i == j:
                y.append(i)
                y.append(i)

