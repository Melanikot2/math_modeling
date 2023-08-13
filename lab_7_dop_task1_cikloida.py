import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o')

def cikloida_move(R, time):
    t = time

    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

edge = 10
plt.axis('equal')
ax.set_xlim(0, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(cikloida_move(R=5, time=i))

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=100)

ani.save('cikloida_move.png')