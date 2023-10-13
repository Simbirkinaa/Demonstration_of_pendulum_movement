import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Параметры маятника
L = 1.0  # Длина нити
alpha = np.radians(60)  # Угол отклонения в радианах (увеличенный угол)
g = 9.81  # Ускорение свободного падения

# Начальная угловая скорость
theta_dot0 = 0.0

# Время и шаг
t = np.linspace(0, 10, 1000)
dt = t[1] - t[0]

# Функция для решения уравнения движения методом Эйлера
def solve_pendulum_motion(alpha, theta_dot0, L, g, dt):
    theta = [alpha]
    theta_dot = [theta_dot0]

    for i in range(1, len(t)):
        theta_double_dot = -(g / L) * np.sin(theta[i-1])
        theta_dot_new = theta_dot[i-1] + theta_double_dot * dt
        theta_new = theta[i-1] + theta_dot_new * dt

        theta_dot.append(theta_dot_new)
        theta.append(theta_new)

    return theta

# Создание анимации
fig, ax = plt.subplots()
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = [0, L * np.sin(theta[i])]
    y = [0, -L * np.cos(theta[i])]
    line.set_data(x, y)
    return line,

theta = solve_pendulum_motion(alpha, theta_dot0, L, g, dt)
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Колебания математического маятника')
plt.show()
