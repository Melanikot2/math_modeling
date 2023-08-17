import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

astroida_line, = plt.plot([], [], '-', lw=2)
dote, = plt.plot([], [], 'o', lw=10)
ball, = plt.plot([], [], '-', lw=2)
big_circle, = plt.plot([], [], '-')

def ball_move(R, t):
    phi = np.linspace(0, 2*np.pi, 1000)
    x_ball = R * np.cos(phi) + 3 * R * np.cos(t)
    y_ball = R * np.sin(phi) + 3 * R * np.sin(t)

    x_circle = 4 * R * np.cos(phi)
    y_circle = 4 * R * np.sin(phi)
    return x_ball, y_ball, x_circle, y_circle

big_circle.set_data(ball_move(R=5, t=0)[2], ball_move(R=5, t=0)[3])

def astroida_move(t, R):
    alpha = np.linspace(0, 57, 500)
    x_line = 4 * R * np.cos(alpha)**3
    y_line = 4 * R * np.sin(alpha)**3

    x = 4 * R * np.cos(t)**3
    y = 4 * R * np.sin(t)**3
    return x, y, x_line, y_line

plt.axis('equal')
ax.set_xlim(-50, 50)
ax.set_ylim(-40, 40)

x, y = [], []
x_ball, y_ball = [], []
x_line, y_line = [], []

def animate(i):
    x.append(astroida_move(R=5, t=i)[0])
    y.append(astroida_move(R=5, t=i)[1])
    x_ball.append(ball_move(R=5, t=i)[0])
    y_ball.append(ball_move(R=5, t=i)[1])
    x_line.append(astroida_move(R=5, t=i)[2])
    y_line.append(astroida_move(R=5, t=i)[3])

    astroida_line.set_data(x_line[i], y_line[i])
    dote.set_data(x[i], y[i])
    ball.set_data(x_ball[i], y_ball[i])

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)

ani.save('astroida_move.gif')