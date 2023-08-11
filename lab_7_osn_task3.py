import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

butterfly = plt.plot([], [])

xdata, ydata = [0], [0]

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def butterfly(t=np.linspace(0, 12*np.pi, 10000)):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2)
    y = alpha * t * np.sin(phi)
    return x, y

plt.axis('equal')

def animate(i):
    ball.set_data(butterfly(t=i, alpha=2))

ani = animation.FuncAnimation(fig, animate, frames = 500, interval=1000)

ani.save('butterfly.gif')