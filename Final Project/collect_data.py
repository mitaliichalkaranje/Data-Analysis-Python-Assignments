
# coding: utf-8

# In[2]:

#Popular video counts
import requests
import json
import pandas as pd
import csv
r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=50&chart=mostPopular&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
data = json.loads(r.text)
print(data)
nextPage=data['nextPageToken']
count=0
dfCount=0
d= pd.DataFrame()
for k in range(1,3):
    print("request",k,nextPage)
    r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=50&chart=mostPopular&pageToken="+nextPage+"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
    data = json.loads(r.text)
    nextPage=data['nextPageToken']
    for items in data['items']:
        tempDF=pd.DataFrame([items['id']],columns=['id'])
        d = pd.concat([d,tempDF])
d.to_csv('data/popularVideosList.csv', sep=',', encoding='utf-8')

#Get a List of pupular video IDs
d=pd.read_csv('data/popularVideosList.csv', index_col=0)
list1=str(d[1:51]['id'].tolist())
list1 = list1.replace(" ","")
list1 = list1.replace("[","")
list1 = list1.replace("]","")
list1 = list1.replace("'","")
list2=str(d[51:100]['id'].tolist())
list2 = list2.replace(" ","")
list2 = list2.replace("[","")
list2 = list2.replace("]","")
list2 = list2.replace("'","")

d= pd.DataFrame()
r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&maxResults=50&id="+list1+"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
data1=json.loads(r.text)
r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&maxResults=50&id="+list2+"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
data2=json.loads(r.text)
for items in data1['items']:
    tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'viewcount':[items['statistics']['viewCount']],'Published Date':[items['snippet']['publishedAt']]})
    d = pd.concat([d,tempDF])
for items in data2['items']:
    tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'viewcount':[items['statistics']['viewCount']],'Published Date':[items['snippet']['publishedAt']]})
    d = pd.concat([d,tempDF])
d.to_csv('data/popularVideosCount.csv', sep=',', encoding='utf-8')


# In[53]:

#Import Languges and Regions

import requests
import json
import pandas as pd
import csv
r = requests.get("https://www.googleapis.com/youtube/v3/i18nRegions?part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
data = json.loads(r.text)
d=pd.DataFrame()
for items in data['items']:
        tempDF=pd.DataFrame({'RegionID':[items['id']],'RegionName':[items['snippet']['name']]})
        d = pd.concat([d,tempDF])
d.to_csv('data/RegionCode.csv', sep=',', encoding='utf-8',index=False)

r = requests.get("https://www.googleapis.com/youtube/v3/i18nLanguages?part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
data = json.loads(r.text)
d=pd.DataFrame()
for items in data['items']:
        tempDF=pd.DataFrame({'LanguageID':[items['id']],'LanguageName':[items['snippet']['name']]})
        d = pd.concat([d,tempDF])
        #print(d)
d.to_csv('data/LanguageCode.csv', sep=',', encoding='utf-8',index=False)



# In[48]:

import pandas as pd
import math
import time
import requests
d=pd.read_csv('data/RegionCode.csv')
total=len(d)
dat=pd.DataFrame()
for i in d.index:
    print(d.ix[i]['RegionName'])
    r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&regionCode="+d.ix[i]['RegionID']+"&chart=mostPopular&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
    data = json.loads(r.text)
    nextPage=data['nextPageToken']
    totalResults=math.floor(data['pageInfo']['totalResults']/5)-1
    print(totalResults)
    for items in data['items']:
        title=items['snippet']['title']
        if title!='Deleted video':
            tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionName'],'CategoryId':[items['snippet']['categoryId']],'VideoID':[items['id']],'ViewCount':[items['statistics']['viewCount']],'CountryCode':d.ix[i]['RegionID']})
            dat = pd.concat([dat,tempDF])
          
    for i in range(1,totalResults):
        r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&regionCode="+d.ix[i]['RegionID']+"&pageToken="+nextPage+"&chart=mostPopular&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
        data = json.loads(r.text)
        nextPage=data['nextPageToken']
        for items in data['items']:
            title=items['snippet']['title']
            if title!='Deleted video':
                tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionName'],'CategoryId':[items['snippet']['categoryId']],'VideoID':[items['id']],'ViewCount':[items['statistics']['viewCount']],'CountryCode':d.ix[i]['RegionID']})
                dat = pd.concat([dat,tempDF])

dat.to_csv('data/Data.csv', sep=',', encoding='utf-8',index=False)

    


# In[45]:

#Import Categories for every country
import requests
import json
import pandas as pd
d=pd.read_csv('data/RegionCode.csv')
total=len(d)
dat=pd.DataFrame()
for i in d.index:
    r = requests.get("https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode="+d.ix[i]['RegionID']+"&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
    data = json.loads(r.text)
    for items in data['items']:
        tempDF=pd.DataFrame({'CategoryID':[items['id']],'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionID']})
        dat = pd.concat([dat,tempDF])
dat.to_csv('data/VideoCategories.csv', sep=',', encoding='utf-8',index=False)


# In[1]:

#Import all videos
import pandas as pd
import math
import time
import requests
import json
d=pd.read_csv('data/RegionCode.csv')
total=len(d)
dat=pd.DataFrame()
for i in d.index:
    print(d.ix[i]['RegionID'])
    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&regionCode="+d.ix[i]['RegionID']+"&maxResults=50&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
    data = json.loads(r.text)
    if r.status_code==200:
        nextPage=data['nextPageToken']
        print(nextPage)
        country=data['regionCode']
        totalResults=math.floor(data['pageInfo']['totalResults']/50)-1
        print(totalResults)
        for items in data['items']:
            title=items['snippet']['title']
            if title!='Deleted video':
                tempDF=pd.DataFrame({'Country':[country],'Title':[items['snippet']['title']],'Published At':[items['snippet']['publishedAt']]})
                dat = pd.concat([dat,tempDF])
          
        for i in range(1,19):
            print(i)
            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&regionCode="+d.ix[i]['RegionID']+"&maxResults=50&pageToken="+nextPage+"&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak")
            data = json.loads(r.text)
            if r.status_code==200:
                print(nextPage)
                nextPage=data['nextPageToken']
                print(nextPage)
                country=data['regionCode']
                for items in data['items']:
                    title=items['snippet']['title']
                    if title!='Deleted video':
                        tempDF=pd.DataFrame({'Country':[country],'Title':[items['snippet']['title']],'Published At':[items['snippet']['publishedAt']]})
                        dat = pd.concat([dat,tempDF])
            else:
                dat.to_csv('data/AllVideos.csv', sep=',', encoding='utf-8',index=False)    

dat.to_csv('data/AllVideos.csv', sep=',', encoding='utf-8',index=False)


# In[27]:

r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&regionCode=DZ&key=AIzaSyD_MXfoSS6zCk1KMkCVkQXB3ZR-NGmCzDo")
print(json.loads(r.text))


# In[3]:

import plotly.plotly as py
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +    'Beef '+df['beef']+' Dairy '+df['dairy']+'<br>'+    'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+    'Wheat '+df['wheat']+' Corn '+df['corn']

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['code'],
        z = df['total exports'].astype(float),
        locationmode = 'USA-states',
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Millions USD")
        ) ]

layout = dict(
        title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict( data=data, layout=layout )
py.iplot( fig, filename='d3-cloropleth-map' )


# In[ ]:




# In[ ]:



