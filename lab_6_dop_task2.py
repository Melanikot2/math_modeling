import matplotlib.pyplot as plt
import numpy as np

def ell(e, p):
    f = np.linspace(-np.pi, np.pi, 5000)
    X = []
    Y = []
    for i in f:
        x = np.cos(p / (1 + e * np.cos(i)))
        y = np.sin(p / (1 + e * np.cos(i)))
        X.append(x)
        Y.append(y)
    
    plt.plot(X, Y)
    plt.savefig('ell.png')

ell(e=0.5, p=10)