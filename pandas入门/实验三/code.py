import pandas as pd
import matplotlib.pyplot as plt

infile = 'bike.csv'
df = pd.read_csv(infile)
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index('datetime')
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['hour'] = df.index.hour

plt.rcParams['font.sans-serif'] = ['SimHei'] #解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False #解决plt负号显示的问题

year = df.groupby(lambda x: x.year).mean()
year[['count']].plot(kind='bar',rot=360)
plt.title('自行车每年租赁数分布图')
plt.show()

quarter = df.groupby('month').mean()
quarter[['count']].plot(kind='bar',rot=360)
plt.title('自行车每月租赁数分布图')
plt.show()

m_bike = df.resample('M').mean()
fig, axes = plt.subplots(2, 1)    #两行一列
m_bike['2011'][['count']].plot(ax=axes[0],sharex=True)  #贡献X轴
m_bike['2012'][['count']].plot(ax=axes[1])
plt.title('自行车每月租赁数分布图')
plt.show()

day = df.groupby('day').mean()
day[['count']].plot(kind='bar',rot=360)
plt.title('自行车每日租赁数分布图')
plt.show()

hour = df.groupby('hour').mean()
hour[['count']].plot(kind='bar',rot=360)
plt.title('自行车每小时租赁数分布图')
plt.show()

weather = df.groupby('weather').mean()
weather[['count']].plot(kind='bar',rot=360)
plt.title('天气情况与自行车租赁数分布图')
plt.show()
