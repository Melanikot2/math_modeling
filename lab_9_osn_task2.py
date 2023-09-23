import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 50, 0.1)

def investicii(n, t):
    dndt = - k * n
    return dndt

n_0 = 1000
k = 0.08

n_t = odeint(investicii, n_0, t)

plt.plot(t, n_t[:, 0], label='Инвестиции')

plt.savefig('investicii.png')