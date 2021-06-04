import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# a*e**(b/x)的拟合
def func(x, a, b):
    return a * np.exp(b / x)


x = np.arange(1, 11, 1)
y = np.array([3.98, 5.1, 5.85, 6.4, 7.4, 8.6, 10, 10.2, 13.1, 14.5])
popt, pcov = curve_fit(func, x, y)
print('拟合系数：\n', popt)
print('最优参数的协方差估计矩阵：\n', pcov)
a = popt[0]
b = popt[1]
y1 = func(x, a, b)
plt.plot(x, y, 'o', label='original values')
plt.plot(x, y1, 'k', label='fit values')
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve_fit')
plt.legend(loc=2)
plt.show()


# a*e**(-b*x)+c的拟合
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


x = np.linspace(0, 4, 50)
y = func(x, 2.5, 1.3, 0.5)
y2 = y + 0.2 * np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, y2)
plt.plot(x, y2, 'o', label='original values')
plt.plot(x, func(x, *popt), 'k', label='fit values')
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve_fit')
plt.legend(loc=1)
plt.show()


# a*sin(x)+b的拟合
def f(x):
    return 2 * np.sin(x) + 3


def func(x, a, b):
    return a * np.sin(x) + b


x = np.linspace(-2*np.pi, 2*np.pi)
y3 = f(x) + 0.5 * np.random.randn(len(x))
popt, pcov = curve_fit(func, x, y3)
plt.scatter(x, y3, c='g', label='original values')
plt.plot(x, func(x, *popt), 'b--', label='fit values')
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve_fit')
plt.legend(loc=1)
plt.show()
