import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

dote, = plt.plot([], [], 'o', lw=15)
ball, = plt.plot([], [], '-', lw=2)
cikloida_line, = plt.plot([], [], '-', lw=2, color='r')
line, = plt.plot([0, 80], [0, 0], color='b')

def ball_move(R, t):
    phi = np.linspace(0, 2*np.pi, 1000)
    x_ball = R * np.cos(phi) + t / 600 * 190 * np.pi * R
    y_ball = R * np.sin(phi) + R
    return x_ball, y_ball

def cikloida_move(t, R):
    alpha = np.linspace(0, 40, 500)
    x_line = R * (alpha - np.sin(alpha))
    y_line = R * (1 - np.cos(alpha))
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y, x_line, y_line

plt.axis('equal')
ax.set_xlim(-10, 80)
ax.set_ylim(-20, 40)

x, y = [], []
x_ball, y_ball = [], []
x_line, y_line = [], []

def animate(i):
    x.append(cikloida_move(R=5, t=i)[0])
    y.append(cikloida_move(R=5, t=i)[1])
    x_ball.append(ball_move(R=5, t=i)[0])
    y_ball.append(ball_move(R=5, t=i)[1])
    x_line.append(cikloida_move(R=5, t=i)[2])
    y_line.append(cikloida_move(R=5, t=i)[3])

    dote.set_data(x[i], y[i])
    ball.set_data(x_ball[i], y_ball[i])
    cikloida_line.set_data(x_line[i], y_line[i])

ani = animation.FuncAnimation(fig, animate, frames=50, interval=100)

ani.save('1.gif')