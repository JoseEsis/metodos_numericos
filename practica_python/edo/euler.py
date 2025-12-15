# MÉTODO DE EULER – UN EJERCICIO

import math
import pandas as pd


# Definición del método de Euler
def euler_method(f, x0, y0, h, steps):
    xs = [x0]
    ys = [y0]
    x, y = x0, y0

    for i in range(steps):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)

    return xs, ys


# ===============================
# EJERCICIO
# y' = y
# y(0) = 1
# h = 0.1
# pasos = 2
# ===============================

f = lambda x, y: y
x0 = 0.0
y0 = 1.0
h = 0.1
steps = 2

# Euler
xs, ys_euler = euler_method(f, x0, y0, h, steps)

# Solución exacta: y = e^x
ys_exact = [math.exp(x) for x in xs]

# Tabla de resultados
tabla = pd.DataFrame({"x": xs, "y_Euler": ys_euler, "y_Exacta": ys_exact})

tabla["Error"] = tabla["y_Exacta"] - tabla["y_Euler"]

# Mostrar resultados
pd.set_option("display.float_format", "{:.6f}".format)

print("MÉTODO DE EULER – EJERCICIO")
print(tabla.to_string(index=False))
