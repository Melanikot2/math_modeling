import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

dich = plt.plot([], [], '-')

xdata, ydata = [0.1], [0.1]

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def anim(n=np.arange(0, 20, 1)):
    C = 0.3
    D = 0.33
    a = xdata[n]
    b = ydata[n]
    xdata.append(a ** 2 - b ** 2 + C)
    ydata.append(2 * a * b + D)
    dich.set_data(xdata, ydata)
    return dich,

plt.axis('equal')

ani = animation.FuncAnimation(fig, anim, frames=1000, interval=30)

ani.save('dich.gif')