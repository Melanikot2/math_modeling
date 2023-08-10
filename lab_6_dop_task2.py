import matplotlib.pyplot as plt
import numpy as np

def ell(e, p):
    f = np.linspace(-np.pi, np.pi, 5000)
    
    
    x = np.cos(p / (1 + e * np.cos(f)))
    y = np.sin(p / (1 + e * np.cos(f)))
    
    
    plt.plot(x, y)
    plt.savefig('ell.png')

ell(e=0.5, p=10)