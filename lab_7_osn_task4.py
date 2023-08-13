import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

dich = plt.plot([], [], '-')

xdata, ydata = [0.1], [0.1]

ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)

def anim(n):
    C=0.3
    D=0.33
    for i in range(1, n + 1, 1):
        xdata.append(xdata[i-1] ** 2 - ydata[i-1] ** 2 + C)
        ydata.append(2 * xdata[i-1] * ydata[i-1] + D)
    dich.set_data(xdata, ydata)
    return dich,

plt.axis('equal')

ani = animation.FuncAnimation(fig, anim, frames=800, n=10, interval=100)

ani.save('dich.gif')