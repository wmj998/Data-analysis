from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data[0:6]
print('原始数据：\n', data)

data = MinMaxScaler().fit_transform(data)
print('最小-最大规范化后的数据：\n', data)
