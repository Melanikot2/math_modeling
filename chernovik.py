import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
cikloida_line, = plt.plot([], [], 'o')
ball, = plt.plot([], [], 'o')

def cikloida_move(R, t):
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y


edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
x, y = [], []

def animate_line(i):
    x.append(cikloida_move(R=3, t=i)[0])
    y.append(cikloida_move(R=3, t=i)[1])
    cikloida_line.set_data(x[i], y[i])



ani = animation.FuncAnimation(fig, animate_line, frames=100, interval=300)

ani.save('cikloida_move.gif')
