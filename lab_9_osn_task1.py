import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 1)

def bacterii(n, t):
    dndt = k * n
    tx = dndt / (10 * n_0)
    print(tx)
    return dndt

n_0 = 10
k = 5

n_t = odeint(bacterii, n_0, t)

plt.plot(t, n_t[:, 0], label='Бактерии')

plt.savefig('bacterii.png')

