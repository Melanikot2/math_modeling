import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object = plt.plot([], [], 'o', lw=2)

xdata, ydata = [0], [0]

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def circle(a, f):
    for i in np.arange(0, 50, 1):
        xdata.append(a * i * np.cos(f))
        ydata.append(a * i * np.sin(f))
        anim_object.set_data(xdata, ydata)
    return anim_object

ani = FuncAnimation(fig, circle, a=2, f=np.arange(0, 2 * np.pi, 0.1), interval=500)


ani.save('circle.gif')