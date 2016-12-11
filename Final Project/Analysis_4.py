
# coding: utf-8

# In[29]:

#Monthly Frequency of videos Published
import tkinter as tk
from IPython.display import clear_output
import pandas as pd
import matplotlib.pyplot as plt
country=pd.read_csv('data/RegionCode.csv')

OPTIONS =country.set_index('RegionName')['RegionID'].to_dict()

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.var = tk.StringVar()
        self.var.set('Select Country')
        self.option = tk.OptionMenu(master, self.var, *OPTIONS.keys())
        self.option.pack()
        def ok():
            if self.var.get()=='Select Country':
                try:
                    self.label.destroy()
                except (NameError, AttributeError):
                    pass
                self.label = tk.Label(master,text="Please select a Country..!")
                self.label.pack()
            else:
                try:
                    self.label.destroy()
                except (NameError, AttributeError):
                    pass
                print(self.var.get())
                self.label = tk.Label(master,text="Please see the console")
                self.label.pack()
                d=pd.read_csv('data/Data.csv')
                result=pd.DataFrame()
                #result=d.groupby(['CategoryId','Country']).count()
                result=pd.read_csv('data/AllVideos.csv')
                result['Published At']=pd.to_datetime(result['Published At']).dt.month
                result=result[result['Country']==OPTIONS[self.var.get()]]
                print(result)
                result=pd.DataFrame({'VideoCount' : result.groupby( [ 'Published At','Country'] ).size()}).reset_index() 
                clear_output()
                print(result)
                result.to_csv('Analysis/analysis_4('+self.var.get()+').csv', sep=',', encoding='utf-8',index=True) 
                result.plot.area(x='Published At',y='VideoCount')
                plt.title('Monthly Frequency of videos Published for'+self.var.get())
                plt.show()
                
        self.button=tk.Button(master, text="OK", command=ok)
        self.button.pack()
        
root = tk.Tk()
app = App(root)
root.mainloop()



# In[ ]:



