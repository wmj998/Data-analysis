import matplotlib.pyplot as plt
import numpy as np

# 直线拟合
x = np.linspace(100, 200, 30)
y = x + np.random.random_integers(5, 20, 30)
p1 = np.polyfit(x, y, deg=1)
print(p1)
q1 = np.polyval(p1, x)
plt.plot(x, y, 'o')
plt.plot(x, q1, 'k')
plt.show()

# 抛物线拟合
p2 = np.polyfit(x, y, deg=2)
print(p2)
q2 = np.polyval(p2, x)
plt.plot(x, y, 'o')
plt.plot(x, q2, 'k')
plt.show()

# 3阶多项式拟合
p3 = np.polyfit(x, y, deg=3)
print(p3)
q3 = np.polyval(p3, x)
plt.plot(x, y, 'o')
plt.plot(x, q3, 'k')
plt.show()
