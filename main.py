import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pendulum_module import solve_pendulum_motion

# Параметры маятника:
# L - длина нити; alpha - угол отклонения (в радианах)
# g - ускорение свободного падения; theta_dot0 - Начальная угловая скорость
# t - время; dt - шаг
L = 1.0
alpha = np.radians(60)
g = 9.81
theta_dot0 = 0.0

t = np.linspace(0, 10, 400)
dt = t[1] - t[0]

# Создание анимации
fig, ax = plt.subplots()
# установка горизонтальных и вертикальных пределов графика
# в диапазоне от -L до L
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)

# Отрисовка нити
line, = ax.plot([], [], '-', lw=2, color='blue')

# Отрисовка точки опоры
ax.plot(0, 0, 'o', markersize=5, color='blue')

# Отрисовка шарика
ball, = ax.plot([], [], 'o-', lw=2, markersize=10, color='red')

# Функция init() иницализирует анимацию. Внутри нее настраиваются
# начальные значения для элементов line и ball
def init():
    line.set_data([], [])
    ball.set_data([], [])
    return line, ball


# Функция animate(i) вызывается для каждого кадра анимации,
# внутри нее обновляются данные элементов ball и line, а именно
# координаты нити маятника и координаты шарика
def animate(i):
    x = [0, L * np.sin(theta[i])]
    y = [0, -L * np.cos(theta[i])]
    line.set_data(x, y)
    ball.set_data([x[1]], [y[1]])
    return line, ball

theta = solve_pendulum_motion(alpha, theta_dot0, L, g, t, dt)
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Колебания математического маятника')
plt.show()
