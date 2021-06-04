from scipy.interpolate import lagrange
x = [-2, 0, 1, 2]
y = [17, 1, 2, 17]
a = lagrange(x, y)
print('插值函数的阶：', a.order)
print('插值函数的系数：', a[3], a[2], a[1], a[0])
print(a)
print(a(0.6))
