import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

cikloida_line, = plt.plot([], [], '-', lw=2)
dote, = plt.plot([], [], 'o', lw=10)
ball, = plt.plot([], [], '-')
line, = plt.plot([0, 80], [0, 0])

def cikloida_move(time, R):
    t = time
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
     
    phi = np.linspace(0, 2*np.pi, 1000)
    x_ball = R * np.cos(phi) * t 
    y_ball = R * np.sin(phi)
    return x, y, x_ball, y_ball

plt.axis('equal')
ax.set_xlim(-10, 80)
ax.set_ylim(-20, 40)

x, y = [], []
x_ball, y_ball = [], []

def animate(i):
    x.append(cikloida_move(R=5, time=i)[0])
    y.append(cikloida_move(R=5, time=i)[1])
    cikloida_line.set_data(x[:i], y[:i])
    dote.set_data(x[i], y[i])
    ball.set_data(x_ball, y_ball)

    
    
ani = animation.FuncAnimation(fig, animate, frames=100, interval=60)

ani.save('chernovik.gif')