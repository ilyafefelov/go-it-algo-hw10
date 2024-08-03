import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
def monte_carlo_integration(f, a, b, num_points=10000):
    """
    Approximates the definite integral of a function using Monte Carlo integration.

    Parameters:
    f (function): The function to integrate.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    num_points (int, optional): The number of random points to generate. Defaults to 10000.

    Returns:
    float: The approximate value of the definite integral.
    """
    x_random = np.random.uniform(a, b, num_points)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Обчислення інтеграла методом Монте-Карло
mc_integral = monte_carlo_integration(f, a, b)
print(f"Monte Carlo Integral: {mc_integral}")

# Перевірка з функцією quad
quad_integral, _ = spi.quad(f, a, b)
print(f"Quad Integral: {quad_integral}")

# Побудова графіка
x = np.linspace(a, b, 400)
y = f(x)
ix = np.linspace(a, b)
iy = f(ix)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Plot of integration f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
