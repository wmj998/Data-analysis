import pandas as pd
import numpy as np
rng = pd.date_range('20200202', periods=2)
s1 = pd.Series(np.arange(1,3), index=rng)

s1_6h_asfreq = s1.resample('6H').asfreq()
print(s1_6h_asfreq)
s1_6h_pad = s1.resample('6H').pad()
print(s1_6h_pad)
s1_6h_ffill = s1.resample('6H').ffill()
print(s1_6h_ffill)
s1_6h_bfill = s1.resample('6H').bfill()
print(s1_6h_bfill)
