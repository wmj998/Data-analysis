from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data[0:6]
print('原始数据：\n', data)

data = StandardScaler().fit_transform(data)
print('标准差标准化后的数据：\n', data)
