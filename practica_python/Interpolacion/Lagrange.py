import numpy as np
import matplotlib.pyplot as plt

x_points = np.array([0.0, 1.0, 3.0])
y_points = np.array([1.0, 2.0, 0.0])
x_eval = 2.0


def lagrange(xs, ys):
    n = len(xs)
    result = np.zeros(n)

    for i in range(n):
        xs_excl = np.delete(xs, i)
        numer_coeffs = np.poly(xs_excl)
        denom = np.prod(xs[i] - xs_excl)

        if len(numer_coeffs) < len(result):
            numer_coeffs = np.pad(
                numer_coeffs, (len(result) - len(numer_coeffs), 0), "constant"
            )

        result = result + ys[i] * numer_coeffs / denom
    return result


coeff = lagrange(x_points, y_points)

P = np.poly1d(coeff)
y_eval = P(x_eval)

print(P)
print(f"P({x_eval}) = {y_eval}")

x_vals = np.linspace(min(x_points) - 1, max(x_points) + 1, 400)
y_vals = P(x_vals)

plt.plot(x_vals, y_vals, color="blue")
plt.scatter(x_points, y_points, color="red")
plt.scatter([x_eval], [y_eval], color="green")

plt.grid(True)
plt.show()
