import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(1, 7.5, 0.5)
a, b, c = 1, 2, 1

def y(x):
    if x < 3:
        return a * x**2 + b * x + c
    elif x == 3:
        return 2 * x + c * x + b
    else:
        return 3 * x**2 - x - 1

y_values = np.array([y(x) for x in x_values])

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, marker='o', color='orange', linestyle='-')
plt.title("Parça-parça Funksiya Qrafiki")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axvline(x=3, color='gray', linestyle='--')
plt.show()
