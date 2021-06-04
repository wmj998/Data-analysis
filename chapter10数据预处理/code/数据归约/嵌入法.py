# 基于惩罚项的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
# 带L2惩罚项的逻辑回归作为基模型的特征选择
data = SelectFromModel(LogisticRegression(penalty="l2", C=0.1)).fit_transform(iris.data, iris.target)
print('基于惩罚项的特征选择法特征选择后的数据：\n', data[0:5])


# 基于树模型的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris

iris = load_iris()
data = SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)
print('基于树模型的特征选择法特征选择后的数据：\n', data[0:5])
