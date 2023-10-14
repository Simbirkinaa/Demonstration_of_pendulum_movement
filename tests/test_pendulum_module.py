import unittest
import numpy as np
from pendulum_module import solve_pendulum_motion


class TestPendulumModule(unittest.TestCase):

    def test_pendulum_motion(self):
        # Проверка, что функция возвращает список углов правильной длины
        L = 1.0
        alpha = np.radians(60)
        g = 9.81
        theta_dot0 = 0.0
        t = np.linspace(0, 10, 1000)
        dt = t[1] - t[0]
        theta = solve_pendulum_motion(alpha, theta_dot0, L, g, t, dt)
        self.assertEqual(len(theta), len(t))

    def test_pendulum_motion_initial_conditions(self):
        # Проверка начальных условий
        L = 1.0
        alpha = np.radians(0)  # Начальное отклонение
        g = 9.81
        theta_dot0 = 0.0
        t = np.linspace(0, 10, 1000)
        dt = t[1] - t[0]
        theta = solve_pendulum_motion(alpha, theta_dot0, L, g, t, dt)
        self.assertEqual(theta[0], alpha)  # 1-й угол должен равняться начальному отклонению


if __name__ == '__main__':
    unittest.main()
