#Final Project

Topic: Analysis on youtube data

API Reference: youtube data API - https://developers.google.com/youtube/v3/docs/

Packages used: matplotlib, pandas, math, requests, json, tkinter

Data Collection:
    API Methods used:
    1. search
    2. videoCategories
    3. videos
    Data Files created after collection:
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

    2. What are number of Videos Published yearwise for selected country?
        >