
# coding: utf-8

# In[ ]:

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
                self.label = tk.Label(master,text="value is"+self.var.get())
                self.label.pack()
                d=pd.read_csv('data/Data.csv')
                result=pd.DataFrame()
                #result=d.groupby(['CategoryId','Country']).count()
                cat=pd.read_csv('data/VideoCategories.csv')
                result=pd.DataFrame({'VideoCount' : d.groupby( [ 'CategoryId','Country'] ).size()}).reset_index() 
                clear_output()
                final=result[result['Country'] == self.var.get()]
                del final['Country']
                cat=pd.read_csv('data/CategoryNames.csv')
                final1=pd.merge(final,cat, on='CategoryId')
                del final1['CategoryId']
                a=final1.set_index('Title')
                print(a)
                a.to_csv('Analysis/analysis_1('+self.var.get()+').csv', sep=',', encoding='utf-8',index=True) 
                a.plot(kind='pie',autopct='%1.1f%%',fontsize=17,subplots=True,shadow=True)
                plt.axis('equal')
                plt.ylabel('')
                plt.legend(loc='best')
                plt.title('Top Categories of most popular videos in '+self.var.get())
                plt.show()
        self.button=tk.Button(master, text="OK", command=ok)
        self.button.pack()
        
root = tk.Tk()
app = App(root)
root.mainloop()



# In[ ]:



