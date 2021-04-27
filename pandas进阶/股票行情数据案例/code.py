import pandas as pd
import matplotlib.pyplot as plt

#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

infile ='data.xlsx'
df = pd.read_excel(infile)
df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index
df = df[['close']]

df['20天'] = df['close'].rolling(20).mean()
df['50天'] = df['close'].rolling(50).mean()
df['200天'] = df['close'].rolling(200).mean()
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df.plot(grid = True)
plt.legend(loc='upper right')
plt.show()
