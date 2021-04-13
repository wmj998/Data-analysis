import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取文件
infile = 'data.xlsx'
outfile = 'result.xlsx'
pd.set_option('display.unicode.east_asian_width', True)  # 对齐
data_1 = pd.read_excel(infile)

# 预处理
data_1 = data_1.drop(columns='排名')
data_1 = data_1.replace(regex='\(\d\)', value='')
data_1.rename(columns={'进球（点球）':'进球'}, inplace=True)

# 模型
data_1['进球'] = data_1['进球'].astype(int)
data_1['场均时间'] = data_1['出场时间']/data_1['出场次数']
data_1['射正率'] = data_1['射正']/data_1['射门']
data_1['进球率'] = data_1['进球']/data_1['射正']
data_1['综合'] = (data_1['场均时间']/100 + data_1['射正率'] + data_1['进球率'])/3

plt.rcParams['font.sans-serif'] = ['SimHei'] #解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False #解决plt负号显示的问题

# 相关系数，热力图
sns.heatmap(data_1.corr(), annot=True)
plt.show()

# 回归拟合
plt.subplot(2,1,1)
plt.title('场均时间与综合回归拟合', fontsize=15)
sns.regplot('场均时间','综合',data=data_1)
plt.subplot(2,2,3)
plt.title('射正率与综合回归拟合', fontsize=15)
sns.regplot('射正率','综合',data=data_1)
plt.subplot(2,2,4)
plt.title('进球率与综合回归拟合', fontsize=15)
sns.regplot('进球率','综合',data=data_1)
plt.show()

# 球员
data_1.index = data_1['球员']
data_1['综合'].plot(kind='barh')
plt.xlabel('综合')
plt.ylabel('球员')
plt.title('球员综合直方图', fontsize=20)
plt.show()

# 球队
data_2 = data_1.groupby('球队')['综合'].mean().reset_index()
data_2.index = data_2['球队']
data_2['综合'].plot(kind='barh')
plt.xlabel('综合')
plt.ylabel('球队')
plt.title('球队综合直方图', fontsize=20)
plt.show()

# 球队排名
data_2 = data_2.sort_values(by='综合', ascending=False)
data_2['排名'] = data_2['综合'].rank(ascending=False)

# 球员排名
data_1 = data_1.sort_values(by='综合', ascending=False)
data_1['排名'] = data_1['综合'].rank(ascending=False)

writer = pd.ExcelWriter(outfile)
data_1.to_excel(writer, sheet_name='球员排名', index=False)
data_2.to_excel(writer, sheet_name='球队排名', index=False)
writer.save()
