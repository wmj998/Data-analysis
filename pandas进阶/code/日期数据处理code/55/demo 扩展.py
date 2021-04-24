import matplotlib.pylab as plt
import numpy as np
import pandas as pd
index=pd.date_range('20200201','20200215')
np.random.seed(2)
data=np.random.randint(20,size=len(index))
ser_data=pd.Series(data,index=index)
plt.figure(figsize=(15, 5))
ser_data.plot(style='r--')
ser_data.rolling(3).mean().plot(style='b')
plt.show()
