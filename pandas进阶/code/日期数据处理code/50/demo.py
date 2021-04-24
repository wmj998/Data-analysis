import pandas as pd
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('time.xls')
df1 = df.set_index('订单付款时间') #设置“订单付款时间”为索引
df_D=df1.resample('D').sum()
df_D.to_excel('dd.xls')
print(df1.resample('W').sum())
print(df1.resample('W',closed='right').sum())
print(df1.resample('W',closed='left').sum())
