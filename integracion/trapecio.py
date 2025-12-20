import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x / (x**4 + 1)


a = 1
b = 3
n = 8
h = (b - a) / n

x = np.zeros(n + 1)
for i in range(n + 1):
    x[i] = a + i * h

s = 0

for i in range(1, n):
    s = s + f(x[i])

T = (h / 2.0) * (f(a) + 2 * s + f(b))

fs = f(x)
print("Resultado: ", T)
print("Puntos: ", x)
print("f(x): ", fs)
plt.plot(x, f(x), color="blue")
plt.scatter(x, f(x), color="red")

plt.grid(True)
plt.legend()
plt.show()
