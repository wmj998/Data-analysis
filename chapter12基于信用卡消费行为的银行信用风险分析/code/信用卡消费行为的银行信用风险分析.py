

# 数据探索分析
import pandas as pd

datafile = '../data/cs-training.csv'
data = pd.read_csv(datafile, index_col=[0])  # 第一列作为行索引
# 产生多个列的汇总统计，T表示转置
data_statistics = data.describe().T
data_statistics['null'] = len(data) - data_statistics['count']  # 计算空值记录数
# 只选取统计结果中的'count'，'null','max','min'四列的内容
data_statistics = data_statistics[['count', 'null', 'max', 'min']]
data_statistics.columns = ['总样本数', '空值数', '最大值', '最小值']  # 重命名列
print(data_statistics)




# 绘制客户年龄直方图的代码如下所示。
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

datafile = '../data/cs-training.csv'
data = pd.read_csv(datafile, index_col=[0])  # 第一列作为行索引
# 对age进行直方图分析
age = data['age']
sns.distplot(age)
plt.xlabel('年龄', fontproperties='Kaiti', fontsize=15)
plt.show()  # 绘制的客户年龄分布图




# 绘制客户月收入直方图
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

datafile = '../data/cs-training.csv'
data = pd.read_csv(datafile, index_col=[0])  # 第一列作为行索引
# 对MonthlyIncome进行直方图分析，为使图形更直观，将x轴范围设置在50000以内
mi = data[data['MonthlyIncome'] < 50000]['MonthlyIncome']
sns.distplot(mi)
plt.xlabel('月收入', fontproperties='Kaiti', fontsize=15)
plt.show()  # 显示绘制的客户月收入分布如图




# 缺失值处理
from sklearn.ensemble import RandomForestClassifier

# 把已有的数值型特征取出来
process_df = data.iloc[:, [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]]
# 分成已知该特征和未知该特征两部分
known = process_df[process_df.MonthlyIncome.notnull()].values
unknown = process_df[process_df.MonthlyIncome.isnull()].values
# X为特征属性值
X = known[:, 1:]
# y为结果标签值
y = known[:, 0]
# 建立RandomForestClassifier模型
RFC = RandomForestClassifier(random_state=0, n_estimators=200, max_depth=3, n_jobs=-1)
RFC.fit(X, y)
# 用得到的模型进行未知特征值预测
predicted = RFC.predict(unknown[:, 1:]).round(0)
# 用得到的预测结果填补原缺失数据
data.loc[(data.MonthlyIncome.isnull()), 'MonthlyIncome'] = predicted
data = data.dropna()  # 删除含有缺失值的记录
data = data.drop_duplicates()  # 删除重复记录
data_statistics = data.describe().T  # 产生多个列的汇总统计，T表示转置
data_statistics['null'] = len(data) - data_statistics['count']  # 计算空值记录数
# 只选取统计结果中的'count'，'null','max','min'四列的内容
data_statistics = data_statistics[['count', 'null', 'max', 'min']]
data_statistics.columns = ['总样本数', '空值数', '最大值', '最小值']  # 重命名列
print(data_statistics)
data.to_csv('../tmp/MissingData.csv', index=False)  # 缺失值处理结果输出到文件




# 异常值处理
data1 = pd.read_csv('../tmp/MissingData.csv')
# 对MonthlyIncome等于0的异常值进行剔除
data1 = data1[data1['MonthlyIncome'] > 0]
# 产生多个列的汇总统计，T表示转置
data1_statistics = data1.describe(include='all').T
# 计算空值记录数
data1_statistics['null'] = len(data1) - data1_statistics['count']
# 只选取统计结果中的'count'，'null','max','min'四列的内容
data1_statistics = data1_statistics[['count', 'null', 'max', 'min']]
data1_statistics.columns = ['总样本数', '空值数', '最大值', '最小值']  # 重命名列
print(data1_statistics)
data1.to_csv('../tmp/AbnormalData.csv', index=False)  # 异常值处理结果输出到文件




import matplotlib.pyplot as plt

data3 = pd.read_csv('../tmp/AbnormalData.csv')
data4 = data3[
    ['NumberOfTime30-59DaysPastDueNotWorse', 'NumberOfTimes90DaysLate', 'NumberOfTime60-89DaysPastDueNotWorse']]
data4.columns = ['Past', 'Late', 'Worse']  # 重命名列
data4.boxplot()  # 绘制箱线图
plt.show()  # 显示绘制的箱线图




# 删除异常值所在的行：
lst = []
for x in [96, 98]:  # 获取异常值所在的行索引
    lst = lst + data4[(data4.Past == x)].index.tolist()
    lst = lst + data4[(data4.Late == x)].index.tolist()
    lst = lst + data4[(data4.Worse == x)].index.tolist()
DeleteAbnormalData = data3.drop(lst)  # 删除异常值所在的行
# 产生多个列的汇总统计
data2_statistics = DeleteAbnormalData.describe(include='all').T
# 计算空值记录数
data2_statistics['null'] = len(DeleteAbnormalData) - data2_statistics['count']
# 只选取统计结果中的'count'，'null','max','min'四列的内容
data2_statistics = data2_statistics[['count', 'null', 'max', 'min']]
data2_statistics.columns = ['总样本数', '空值数', '最大值', '最小值']  # 重命名列
print(data2_statistics)
# 异常值处理结果输出到文件
DeleteAbnormalData.to_csv('../tmp/DeleteAbnormalData.csv', index=False)




# 单变量分析
import pandas as pd

data5 = pd.read_csv('../tmp/DeleteAbnormalData.csv')  # 读取异常处理后的数据集
grouped = data5['SeriousDlqin2yrs'].groupby(data5['SeriousDlqin2yrs']).count()
print(grouped)
print('违约客户占比：%.2f%%' % (100 * grouped[1] / (grouped[0] + grouped[1])))
grouped.plot(kind='bar')  # 显示SeriousDlqin2yrs客户的整体情况
plt.show()




# 绘制年龄与违约客户数变化关系图
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'FangSong'  # FangSong是中文仿宋
matplotlib.rcParams['font.size'] = '18'  # 设置字体大小

lst2 = []
data6 = data5[['age', 'SeriousDlqin2yrs']]
lst1 = [k for k in range(22, 92, 10)]
data7 = data6[data6.SeriousDlqin2yrs == 1]
lst2.append((data7.query('32>age>=22').shape[0]))
lst2.append((data7.query('42>age>=32').shape[0]))
lst2.append((data7.query('52>age>=42').shape[0]))
lst2.append((data7.query('62>age>=52').shape[0]))
lst2.append((data7.query('72>age>=62').shape[0]))
lst2.append((data7.query('82>age>=72').shape[0]))
lst2.append((data7.query('93>age>=82').shape[0]))
plt.plot(lst1, lst2)
plt.xlabel("年龄")
plt.ylabel("违约客户数")
plt.show()  # 显示绘制的年龄与违约客户数的变化关系




# 多变量分析
data5.columns = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
corr = data5.corr(method='pearson')  # 计算各列之间的相关性
print(corr)




# 特征选择
data6 = pd.read_csv('../tmp/DeleteAbnormalData.csv')
# 重新命名列
data6.columns = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
# 获取客户的10个属性和违约情况的相关性
corr = data6.corr().sort_values(by=['x0'], ascending=False)  # x0指代SeriousDlqin2yrs
print(corr)
sns.heatmap(corr, annot=True)
plt.show()



# 逻辑回归分析
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from sklearn import metrics
from sklearn.metrics import classification_report

data7 = pd.read_csv('../tmp/DeleteAbnormalData.csv')
data8 = data7[['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'NumberOfTime30-59DaysPastDueNotWorse',
               'NumberOfTimes90DaysLate', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfDependents']]
Y = data8['SeriousDlqin2yrs']
X = data8.iloc[:, 1:]
# 为了验证模型的拟合效果，需要先对数据集进行切分，分成训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
lr = LR()  # 建立逻辑回归模型
lr.fit(X_train, Y_train)  # 训练模型
y_pred = lr.predict(X_test)  # 用得到的模型对30%的测试集进行预测
# 用均方误差来评价模型优劣
print("模型预测的均方误差:", metrics.mean_squared_error(Y_test, y_pred))
print('预测报告为：\n', classification_report(Y_test, y_pred))

lr = LR().fit(X, Y)
print('模型的平均准确度为', lr.score(X, Y))
