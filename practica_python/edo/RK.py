import math
import matplotlib.pyplot as plt


def f(x, y):
    return -2 * y


t0 = 0
y0 = 1
h = 0.1
steps = 10

ts = [t0]
ys = [y0]

t, y = t0, y0

for i in range(steps):
    k1 = f(t, y)
    k2 = f(t + h / 2, y + (h / 2) * k1)
    k3 = f(t + h / 2, y + (h / 2) * k2)
    k4 = f(t + h, y + h * k3)

    t = t + h

    ts.append(t)
    ys.append(y)


y_rk4 = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
y_exact = [math.exp(-2 * t) for t in ts]
print(f"RK4: y(0.1) = {y_rk4:.6f}")
