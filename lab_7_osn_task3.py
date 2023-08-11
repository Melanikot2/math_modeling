import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

butterfly = plt.plot([], [], '-')

xdata, ydata = [0], [0]

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def butterfly(t=np.linspace(0, 12*np.pi, 10000)):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
    return x, y

plt.axis('equal')

def animate(i):
    butterfly.set_data(butterfly())

ani = animation.FuncAnimation(fig, animate, frames = 500, interval=100)

ani.save('butterfly.gif')