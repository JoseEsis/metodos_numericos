import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([6, 11, 18, 27])

coef = np.polyfit(x, y, 2)
p = np.poly1d(coef)
y_pred = p(x)
ECM = np.mean((y - y_pred) ** 2)

print(coef)
print(p)
print(ECM)

x_fit = np.linspace(min(x), max(x), 180)

plt.plot(x_fit, p(x_fit), color="red")
plt.scatter(x, y, color="blue")

plt.grid(True)
plt.show()
