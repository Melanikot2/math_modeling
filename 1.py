import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
cikloida_line, = plt.plot([], [], 'o')
ball, = plt.plot([], [], 'o')

def cikloida_move(R, time):
    t = time
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

x, y = [], []

def animate_line(i):
    x.append(cikloida_move(R=3, time=i)[0])
    y.append(cikloida_move(R=3, time=i)[1])
    cikloida_line.set_data(x[i], y[i])

def ball_move(R, time):
    x_ball = time
    y_ball = R
    return x_ball, y_ball

x_ball, y_ball = [], []

def animate_ball(i):
    x.append(ball_move(R=3, time=i)[0])
    y.append(ball_move(R=3, time=i)[1])
    ball.set_data(x[i], y[i])


ani = animation.FuncAnimation(fig, animate_ball, frames=100, interval=300)

ani.save('cikloida_move.gif')
