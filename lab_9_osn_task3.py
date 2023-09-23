import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 1)

def move(v, t):
    dvdt = a0 - gamma * v**2 / m
    return dvdt

v_0 = 0
gamma = 3
a0 = 10
m = 2

v_t = odeint(move, v_0, t)

plt.plot(t, v_t[:, 0], label='Движение материальной точки')

plt.savefig('move_tochka.png')