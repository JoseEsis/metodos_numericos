import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return 1.25 * np.sin(x / 2.0) + 3


a = 1
b = 9
n = 2
h = (b - a) / n

x = np.zeros(n + 1)
for i in range(n + 1):
    x[i] = a + i * h

sP = 0
sI = 0

for i in range(1, n):
    if i % 2 == 0:
        sP = sP + f(x[i])
    else:
        sI = sI + f(x[i])

S = (h / 3.0) * (f(a) + 4 * sI + 2 * sP + f(b))

print(S)

plt.plot(x, f(x), color="blue")
plt.scatter(x, f(x), color="red")

plt.grid(True)
plt.show()
