from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()
data = PCA(n_components=2).fit_transform(iris.data)
print('主成分分析法降维后的数据：\n', data[0:5])
