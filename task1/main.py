import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y = -x * np.cos(5 * x)

plt.plot(x, y, linestyle='-', color='b', linewidth=2, label='Y(x) = -x*cos(5*x)')

plt.title('Графік функції Y(x) = -x * cos(5 * x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.legend()

plt.grid()
plt.show()
