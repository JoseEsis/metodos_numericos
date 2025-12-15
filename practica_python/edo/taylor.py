import math
import pandas as pd
import matplotlib.pyplot as plt


def taylor_orden2(f, ypp_func, x0, y0, h, steps):
    xs = [x0]
    ys = [y0]
    x, y = x0, y0

    for i in range(steps):
        y_prime = f(x, y)
        y_pp = ypp_func(x, y, y_prime)

        y = y + h * y_prime + (h**2 / 2.0) * y_pp
        x = x + h

        xs.append(x)
        ys.append(y)

    return xs, ys


# ===============================
# EJERCICIO
# y' = y
# y'' = y
# y(0) = 1
# ===============================

f = lambda x, y: y
ypp = lambda x, y, yp: y  # segunda derivada

x0 = 0.0
y0 = 1.0
h = 0.1
steps = 10

xs, ys_taylor = taylor_orden2(f, ypp, x0, y0, h, steps)

# solución exacta
ys_exact = [math.exp(x) for x in xs]

# tabla
df = pd.DataFrame({"x": xs, "Taylor": ys_taylor, "Exacta": ys_exact})

df["Error"] = df["Exacta"] - df["Taylor"]

print("MÉTODO DE TAYLOR (ORDEN 2)")
print(df.to_string(index=False))

# ===============================
# GRÁFICA
# ===============================

plt.plot(xs, ys_exact, label="Solución exacta  y = e^x", color="blue")
plt.plot(xs, ys_taylor, "o--", label="Taylor orden 2", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Método de Taylor vs Solución Exacta")
plt.legend()
plt.grid(True)
plt.show()
