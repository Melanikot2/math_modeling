import matplotlib.pyplot as plt
import numpy as np

def cikloida(R, t_min, t_max):
    t = np.linspace(t_min, t_max, 500)

    x = R * (t - np.sin(t)**3)
    y = R * (1 - np.cos(t)**3)

    plt.plot(x, y, ls='--')
    plt.axis('equal')
    plt.savefig('cikloida.png')

cikloida(R=5, t_min=0, t_max=40)


def astroida(R, t_min, t_max):
    t = np.linspace(t_min, t_max, 500)

    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('astroida.png')

astroida(R=44, t_min=0, t_max=57)