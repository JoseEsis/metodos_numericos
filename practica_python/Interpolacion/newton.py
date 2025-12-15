import numpy as np
import matplotlib.pyplot as plt


def newton(xs, ys):
    n = len(xs)
    table = np.zeros((n, n))
    table[:, 0] = ys

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (xs[i + j] - xs[i])

    coef = table[0, :]

    return coef, table


def newton_eval(coef, xs, x):
    n = len(coef)
    result = coef[n - 1]

    for k in range(n - 2, -1, -1):
        result = result * (x - xs[k]) + coef[k]

    return result


xs = np.array([1, 0, -3])
ys = np.array([2, 4, -2])

coef, table = newton(xs, ys)


x_test = -0.5
y_eval = newton_eval(coef, xs, x_test)

print(coef)
print(table)

print(f"P({x_test}) = {y_eval}")

x_vals = np.linspace(min(xs) - 0.5, max(xs) + 0.5, 300)
y_vals = []

for x in x_vals:
    y_vals.append(newton_eval(coef, xs, x))

plt.plot(x_vals, y_vals, color="blue")
plt.scatter(xs, ys, color="red")
plt.scatter([x_test], [y_eval], color="green")

plt.grid(True)
plt.show()
