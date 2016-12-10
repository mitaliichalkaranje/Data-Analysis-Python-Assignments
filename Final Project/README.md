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
    
    2. CategoryNames.csv - Consists of video category IDs and their corresponding names collected using 'videoCategories' method of API
    
    3. LanguageCode.csv -  Consists of language IDs and their corresponding names collected using 'i8languages' method of API
    
    4. RegionCode.csv - Consists of Region codes and their corresponding names
    
    5. Data.csv - List of all most popular videos for all available regions collected using videos method

5 Types of Analysis done:

    1. What are the Video Categories for most popular videos in a selected country ?
        >Select a Country from available dropdown menu in the popup window (Implemented using tkinter package)
        >For the selected Country using the Data.csv file, Categories of popular videos for that country are grouped.
        >Using videoCategories.csv file, the titles of corresponding categories are loaded
        >The output is plotted using pie chart
        >Analysis file path: Analysis/analysis_1('CountryName').csv

    2. What are number of Videos Published yearwise for selected country?
        >Select a Country from available dropdown menu in the popup window (Implemented using tkinter package)
        >For the selected Country using the AllVideos.csv file, total number of videos published in that country are grouped.
        >The output is plotted using stacked bar plot.
        >Analysis file path: Analysis/analysis_2('CountryName').csv
       
    3. What is the statistics of countries in publishing videos ?
        >Count the number of published videos for all countries
        >Plot it on map
        >Analysis file path: Analysis/analysis_3.csv
        
    4. For a selected country what is the peak month for published videos ?
        >Select a Country from available dropdown menu in the popup window
        >The Published date column from AllVideos.csv is fetched for corresponding country.
        >For every month, the number of videos published is counted and plotted.
        >Analysis file path: Analysis/analysis_4.csv
    
    5. For a selected country what is average view counts for every month ?
        >Select a Country from available dropdown menu in the popup window
        >Average count for every month for published videos is calculated
<<<<<<< HEAD
        >The result file will contain month and their correspnding average viewcounts
=======
        >The result file will contain month and their correspnding average viewcounts
>>>>>>> 5b8bf66eb0c3f675e5df85b8d6fb6a3eb2f8c130
