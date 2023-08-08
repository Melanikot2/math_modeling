import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball = plt.plot([], [], 'o')


ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def circle(n, frame):
    x = n * frame * np.cos(f))
    ydata.append(n * frame * np.sin(f))
    anim_object.set_data(xdata, ydata)
    return anim_object

ani = FuncAnimation(fig, circle, n=2, frames=np.arange(0, 50, 1), f=np.arange(0, 2 * np.pi, 0.1), interval=500)


ani.save('circle.gif')