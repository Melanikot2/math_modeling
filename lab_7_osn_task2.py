import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ball, = plt.plot([], [], '-')

xdata, ydata = [0], [0]

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def circle(t, alpha):
    phi = np.linspace(0, 2*np.pi, 1000)
    x = alpha * t * np.cos(phi)
    y = alpha * t * np.sin(phi)
    return x, y

plt.axis('equal')

def animate(i):
    ball.set_data(circle(t=i, alpha=2))

ani = animation.FuncAnimation(fig, animate, frames=500, interval=30)

ani.save('circle.gif')