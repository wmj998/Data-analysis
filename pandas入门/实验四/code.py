import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score

infile1 = '广告费.xlsx'
infile2 = '销售表.xlsx'
df1 = pd.read_excel(infile1)
df2 = pd.read_excel(infile2)

df1['投放日期'] = pd.to_datetime(df1['投放日期'])
df1 = df1.set_index('投放日期')
df2 = df2[['日期', '销售码洋']]
df2['日期'] = pd.to_datetime(df2['日期'])
df2 = df2.set_index('日期')
df_x = df1.resample('MS').sum().to_period('M')  # 按月统计广告费支出
df_y = df2.resample('MS').sum().to_period('M')  # 按月统计销售码洋收入

x_train = df_x.values
y_train = df_y.values
l_mod = linear_model.LinearRegression().fit(x_train, y_train)
y_test = l_mod.predict(x_train)
print('模型的预测准确度为：', l_mod.score(x_train, y_train))

score = r2_score(y_train, y_test)
print('模型的预测准确度为：', score)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('电商销售数据分析与预测')
plt.scatter(x_train, y_train, c='r')  # 真实值散点图
plt.plot(x_train, y_test, c='g')  # 预测回归线
plt.xlabel('广告支出（元）')
plt.ylabel('销售码洋（元）')
plt.subplots_adjust(left=0.2)  # 设置图表距画布左边的空白
plt.show()
