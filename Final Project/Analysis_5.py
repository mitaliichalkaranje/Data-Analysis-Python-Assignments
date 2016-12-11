
# coding: utf-8

# In[16]:

#Average View count statistics for most popular video Categories
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('data/Data.csv')
cat=pd.read_csv('data/CategoryNames.csv')
result=pd.DataFrame({'Count' : df.groupby( [ 'CategoryId'] ).size()}).reset_index()
df=df.groupby(['CategoryId']).sum().reset_index()
result=pd.merge(result,df,on='CategoryId')
result=pd.merge(result,cat,on='CategoryId')
result['averageCount']=(result['ViewCount']/result['Count']).astype(int)
result.plot.barh(x='Title',y='averageCount')
plt.title('Average View count statistics for most popular video Categories')
plt.show()
result.to_csv('Analysis/analysis_5.csv', sep=',', encoding='utf-8',index=False) 


# In[ ]:



