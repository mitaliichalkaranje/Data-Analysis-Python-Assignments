
# coding: utf-8

# In[51]:

#Number of most popular videos in a country
import plotly.plotly as py
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
df1=pd.read_csv('data/RegionCode.csv')
allVideos=pd.read_csv('data/AllVideos.csv')
allVideos['Published At']=pd.to_datetime(allVideos['Published At']).dt.year
result=pd.DataFrame({'VideoCount' : allVideos.groupby( ['Published At','Country'] ).size()}).reset_index()
df_new=pd.DataFrame()
result['RegionID']=result['Country']
result=pd.merge(result,df1,on='RegionID')
result = result[result['Published At'] ==2016]
result['COUNTRY']=result['RegionName']
del result['RegionName']
del result['RegionID']
del result['Country']
del result['Published At']
del df['GDP (BILLIONS)']
result=pd.merge(result,df,on='COUNTRY')
result.to_csv('Analysis/analysis_3.csv', sep=',', encoding='utf-8',index=False) 
data = [ dict(
        type = 'choropleth',
        locations = result['CODE'],
        z = result['VideoCount'],
        text = result['COUNTRY'], 
        autocolorscale = True,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = True,
            title = 'Number of Videos'),
      ) ]

layout = dict(
    title = 'Number of most popular videos in 2016',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )


# In[ ]:



