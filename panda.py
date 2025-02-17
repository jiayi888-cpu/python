import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
 "date":pd.date_range('20130102', periods=6),
  "city":['Beijing ', 'ShangHai', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
 "age":[23,44,54,32,34,32],
 "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
  "price":[1200,np.nan,2133,5433,np.nan,4432]},
  columns =['id','date','city','category','age','price'])
#df_sub=df[df["age"]>30][df["price"]>2000]
#df_iloc=df.iloc[:,0]
#print(df.size,df.shape)
#print(df)
df["age"].plot.bar()
plt.show()