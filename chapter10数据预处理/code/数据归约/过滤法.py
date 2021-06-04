# 方差选择法
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
# 参数threshold为方差的阈值
data = VarianceThreshold(threshold=0.2).fit_transform(data)
print('方差选择法特征选择后的数据：\n', data[0:5])


# 相关系数法
import numpy as np
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr
from sklearn.datasets import load_iris

iris = load_iris()
print('原始特征数据：\n', iris.data[0:5])
print('原始类别数据：\n', iris.target[0:5])

m = SelectKBest(lambda X, Y: np.array(list(map(lambda x: pearsonr(x, Y), X.T))).T[0], k=2).fit_transform(iris.data, iris.target)
print('相关系数法特征选择后的数据：\n', m[0:5])


# 卡方检验法
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.datasets import load_iris

iris = load_iris()
data = SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)
print('卡方检验法特征选择后的数据：\n', data[0:5])


# 最大信息系数法
from sklearn.feature_selection import SelectKBest
from minepy import MINE
from sklearn.datasets import load_iris

iris = load_iris()


def mic(x, y):
    m = MINE()
    m.compute_score(x, y)
    return (m.mic(), 0.5)


m = SelectKBest(lambda X, Y: np.array(list(map(lambda x: mic(x, Y), X.T))).T[0], k=2).fit_transform(iris.data, iris.target)
print('最大信息系数法特征选择后的数据：\n', m[0:5])
