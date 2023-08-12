import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

butterfly, = plt.plot([], [], '-')

xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def fly(frame):
    xdata.append(np.sin(frame) * (np.exp(np.cos(frame)) - 2 * np.cos(4 * frame) + np.sin(frame / 12)**5))
    ydata.append(np.cos(frame) * (np.exp(np.cos(frame)) - 2 * np.cos(4 * frame) + np.sin(frame / 12)**5))
    butterfly.set_data(xdata, ydata)
    return butterfly,

plt.axis('equal')

ani = animation.FuncAnimation(fig, fly, frames=np.linspace(0, 12*np.pi, 1000), interval=30)

ani.save('butterfly.gif')