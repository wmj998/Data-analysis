import numpy as np
import matplotlib.pyplot as plt

a = plt.imread("flower.jpg")
b = np.array([0.299,0.587,0.114])
x = np.dot(a, b)  # 将上面的RGB和b数组中的每个元素进行对位相乘，再相加，一定得到的是一个数字L
plt.imshow(x, cmap="gray")
plt.show()
