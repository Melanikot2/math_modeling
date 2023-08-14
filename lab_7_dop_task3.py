import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

star, = plt.plot([], [], '-')

xdata, ydata = [0], [0]

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

def star_move(T, t=np.linspace(0, 4*np.pi, 500)):
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    X = x * np.cos(T) - y * np.sin(T)
    Y = y * np.cos(T) + x * np.sin(T)
    return X, Y

plt.axis('equal')

def animate(i):
    star.set_data(star_move(T=i*np.pi/180))

ani = animation.FuncAnimation(fig, animate, frames=500, interval=30)

ani.save('star.gif')