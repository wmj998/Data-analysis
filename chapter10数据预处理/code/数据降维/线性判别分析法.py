import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

iris = load_iris()
data = LDA(n_components=2).fit_transform(iris.data, iris.target)
print('线性判别分析法降维后的数据：\n', data[0:5])

plt.scatter(data[:, 0], data[:, 1], marker='o', c=iris.target)
plt.show()
