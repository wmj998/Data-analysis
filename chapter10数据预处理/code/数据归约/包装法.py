# 递归消除特征法
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
# 参数estimator用来指定学习模型，参数n_features_to_select为选择的特征个数
data = RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)
print('递归消除特征法特征选择后的数据：\n', data[0:5])
