import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

square, = plt.plot([], [], '-')

xdata, ydata = [0], [0]

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def square_move(T, a=5):
    x = np.array([-a/2, -a/2, a/2, a/2, -a/2])
    y = np.array([-a/2, a/2, a/2, -a/2, -a/2])
    X = x * np.cos(T) - y * np.sin(T)
    Y = y * np.cos(T) + x * np.sin(T)
    return X, Y

plt.axis('equal')

def animate(i):
    square.set_data(square_move(T=i*np.pi/180))

ani = animation.FuncAnimation(fig, animate, frames=500, interval=30)

ani.save('square.gif')