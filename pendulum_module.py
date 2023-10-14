import numpy as np


#  Модуль pendulum_module.py отвечает за решение уравнения движения маятника и
# предоставляет функциональность для вычисления и возвращения углового отклонения
# математического маятника в зависимости от времени

# Функция solve_pendulum_motion использует численный метод (метод Эйлера)
# для решения дифференциального ур-я, описывающего движение мат. маятника.
# Дифференциальное уравнение описывает угловое отклонение маятника
# от вертикального положения в зависимости от времени
def solve_pendulum_motion(alpha, theta_dot0, L, g, t, dt):
    theta = [alpha]
    theta_dot = [theta_dot0]

    for i in range(1, len(t)):
        theta_double_dot = -(g / L) * np.sin(theta[i-1])
        theta_dot_new = theta_dot[i-1] + theta_double_dot * dt
        theta_new = theta[i-1] + theta_dot_new * dt

        theta_dot.append(theta_dot_new)
        theta.append(theta_new)

    return theta
