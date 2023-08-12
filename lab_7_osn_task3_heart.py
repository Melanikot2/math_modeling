import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

heart, = plt.plot([], [], '-')

xdata, ydata = [], []

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def anim(frame):
    xdata.append(16 * np.sin(frame) ** 3)
    ydata.append(13 * np.cos(frame) - 5 * np.cos(2 * frame) - 2 * np.cos(3 * frame) - np.cos(4 * frame))
    heart.set_data(xdata, ydata)
    return heart,

plt.axis('equal')

ani = animation.FuncAnimation(fig, anim, frames=np.linspace(0, 2*np.pi, 200), interval=30)

ani.save('heart.gif')