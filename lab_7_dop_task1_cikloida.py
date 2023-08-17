import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

cikloida_line, = plt.plot([], [], '-', lw=2)
dote, = plt.plot([], [], 'o', lw=10)
ball, = plt.plot([], [], '-', lw=2)
line, = plt.plot([0, 80], [0, 0])

def ball_move(R, t):
    phi = np.linspace(0, 2*np.pi, 1000)
    x_ball = R * np.cos(phi) + t / 600 * 190 * np.pi * R
    y_ball = R * np.sin(phi) + R
    return x_ball, y_ball

def cikloida_move(t, R):
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

plt.axis('equal')
ax.set_xlim(-10, 80)
ax.set_ylim(-20, 40)

x, y = [], []
x_ball, y_ball = [], []


def animate(i):
    x.append(cikloida_move(R=5, t=i)[0])
    y.append(cikloida_move(R=5, t=i)[1])
    x_ball.append(ball_move(R=5, t=i)[0])
    y_ball.append(ball_move(R=5, t=i)[1])

    cikloida_line.set_data(x[:i], y[:i])
    dote.set_data(x[i], y[i])
    ball.set_data(x_ball[i], y_ball[i])
    

ani = animation.FuncAnimation(fig, animate, frames=50, interval=60)

ani.save('cikloida_move.gif')