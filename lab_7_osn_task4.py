import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

dich, = plt.plot([], [], '-', color='r')

x, y = [0.1], [0.1]

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
for i in range(1, 100, 1):
    C = 0.3
    D = 0.33
    x.append(x[i-1] ** 2 - y[i-1] ** 2 + C)
    y.append(2 * x[i-1] * y[i-1] + D)


def anim(i):
    dich.set_data(x[:i], y[:i])


plt.axis('equal')

ani = animation.FuncAnimation(fig, anim, frames=100, interval=300)

ani.save('dich.gif')