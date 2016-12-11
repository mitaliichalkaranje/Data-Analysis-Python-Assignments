
# coding: utf-8

# In[51]:

#'Number of Videos published Yearwise'
import tkinter as tk
from IPython.display import clear_output
import pandas as pd
import matplotlib.pyplot as plt
videos=pd.read_csv('data/AllVideos.csv')
videos['Published At']=pd.to_datetime(videos['Published At'])
videos['Published At']=videos['Published At'].dt.year
result=pd.DataFrame({'VideoCount' : videos.groupby( [ 'Published At']).size()}).reset_index()
result.to_csv('Analysis/analysis_2.csv', sep=',', encoding='utf-8',index=False) 
result.plot.bar(x='Published At',y='VideoCount')
plt.xlabel('Year')
plt.ylabel('Number of Videos')
plt.title('Number of Videos published Yearwise')
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



