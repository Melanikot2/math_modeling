import matplotlib.pyplot as plt
import numpy as np

def ladder(n):
    x = []
    y = [0]
    
    for i in range(n+1):
        x.append(i)
        x.append(i)
    
    for j in range(1, n+1, 1):
        y.append(j)
        y.append(j)
    y.append(n)

    plt.plot(x, y, color='w')
    plt.title(f'Лесенка из {n} ступенек')
    plt.axis('equal')
    plt.savefig('ladder.png')

ladder(n=7)