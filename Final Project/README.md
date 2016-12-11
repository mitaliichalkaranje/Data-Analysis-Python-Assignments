#Final Project

Topic: Analysis on youtube data

API Reference: youtube data API - https://developers.google.com/youtube/v3/docs/

Packages used: matplotlib, pandas, math, requests, json, tkinter

Data Collection:
    
    Path for data collection script - FinalProject/collect_data.py

    API Methods used:
    
    1. search
    
    2. videoCategories
    
    3. videos
    
Data Files created after collection in Data folder:
    1. AllVideos.csv - consists of all video details collected using 'search' method of API    

<img width="348" alt="allvideos" src="https://cloud.githubusercontent.com/assets/22486197/21080677/7e8c7950-bf83-11e6-891a-9184f860e855.PNG">    
    2. CategoryNames.csv - Consists of video category IDs and their corresponding names collected using 'videoCategories' method of API

<img width="144" alt="categorynames" src="https://cloud.githubusercontent.com/assets/22486197/21080714/0addab86-bf84-11e6-81da-00c378c732a4.PNG">    
    3. LanguageCode.csv -  Consists of language IDs and their corresponding names collected using 'i8languages' method of API

<img width="164" alt="languagecode" src="https://cloud.githubusercontent.com/assets/22486197/21080723/5ac17722-bf84-11e6-990a-d4c7b670d6f2.PNG">   
    4. RegionCode.csv - Consists of Region codes and their corresponding names

<img width="151" alt="regioncode" src="https://cloud.githubusercontent.com/assets/22486197/21080726/694f9328-bf84-11e6-82aa-59c85e3ffce8.PNG">
    5. Data.csv - List of all most popular videos for all available regions collected using videos method

<img width="530" alt="data" src="https://cloud.githubusercontent.com/assets/22486197/21080729/78994c20-bf84-11e6-912a-4a2762d7fa64.PNG">

5 Types of Analysis done:

    1. What are the Video Categories for most popular videos in a selected country ?
    
        >Select a Country from available dropdown menu in the popup window (Implemented using tkinter package)      
<img width="174" alt="analysis1_1" src="https://cloud.githubusercontent.com/assets/22486197/21080703/c6a720b4-bf83-11e6-8f43-b0c65529b1dd.PNG">
<img width="325" alt="analysis1_3" src="https://cloud.githubusercontent.com/assets/22486197/21080752/d8650112-bf84-11e6-93df-f91d6d984d4e.PNG">

        >For the selected Country using the Data.csv file, Categories of popular videos for that country are grouped.
        
        >Using videoCategories.csv file, the titles of corresponding categories are loaded
        
        >The output is plotted using pie chart 
<img width="613" alt="analysis1_2" src="https://cloud.githubusercontent.com/assets/22486197/21080758/ff7d702c-bf84-11e6-8e5d-8b992535b458.PNG">
        Analysis file path: Analysis/analysis_1('CountryName').csv

    2. What are number of Videos Published yearwise for selected country?
    
        >Select a Country from available dropdown menu in the popup window       
<img width="174" alt="analysis1_1" src="https://cloud.githubusercontent.com/assets/22486197/21080703/c6a720b4-bf83-11e6-8f43-b0c65529b1dd.PNG"><img width="325" alt="analysis1_3" src="https://cloud.githubusercontent.com/assets/22486197/21080752/d8650112-bf84-11e6-93df-f91d6d984d4e.PNG">


        >For the selected Country using the AllVideos.csv file, total number of videos published in that country are grouped.
    
        >The output is plotted using stacked bar plot.
<img width="374" alt="analysis2" src="https://cloud.githubusercontent.com/assets/22486197/21080835/6cb5f4e6-bf87-11e6-9af2-155d0b8c4012.PNG">
        Analysis file path: Analysis/analysis_2('CountryName').csv
       
    3. What is the statistics of countries in publishing videos in 2016 ?
    
        >The total number of most popular videos published in a country is calculated
        
        >The statictics is plotted on a World Map:
<img width="603" alt="analysis_worldmap" src="https://cloud.githubusercontent.com/assets/22486197/21080881/4c4215ae-bf88-11e6-9506-14e8bf82382a.PNG">        
        Analysis file path: Analysis/analysis_3.csv
        
    4. For a selected country what is the peak month for published videos ?
    
        >Select a Country from available dropdown menu in the popup window
<img width="174" alt="analysis1_1" src="https://cloud.githubusercontent.com/assets/22486197/21080703/c6a720b4-bf83-11e6-8f43-b0c65529b1dd.PNG">
<img width="325" alt="analysis1_3" src="https://cloud.githubusercontent.com/assets/22486197/21080752/d8650112-bf84-11e6-93df-f91d6d984d4e.PNG">

        >The Published date column from AllVideos.csv is fetched for corresponding country.
        
        >For every month, the number of videos published is counted and plotted.
<img width="354" alt="analysis4" src="https://cloud.githubusercontent.com/assets/22486197/21080806/b5a0c858-bf86-11e6-950a-a8c3660146b7.png">
         Analysis file path: Analysis/analysis_4.csv
    
    5. What is the average view count for most popular videos ?
    
        >The average fr view counts is calculated by summing up the view counts for most popular videos based on their categories
 <img width="491" alt="analysis5" src="https://cloud.githubusercontent.com/assets/22486197/21080826/1db150fc-bf87-11e6-90e4-1cfb5eeefbca.png">   
        Analysis file path: Analysis/analysis_4.csv
