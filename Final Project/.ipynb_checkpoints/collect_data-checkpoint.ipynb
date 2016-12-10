{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "request 1 CDIQAA\n",
      "request 2 CGQQAA\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "import csv\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=50&chart=mostPopular&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data = json.loads(r.text)\n",
    "nextPage=data['nextPageToken']\n",
    "count=0\n",
    "dfCount=0\n",
    "d= pd.DataFrame()\n",
    "for k in range(1,3):\n",
    "    print(\"request\",k,nextPage)\n",
    "    r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=50&chart=mostPopular&pageToken=\"+nextPage+\"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "    data = json.loads(r.text)\n",
    "    nextPage=data['nextPageToken']\n",
    "    for items in data['items']:\n",
    "        tempDF=pd.DataFrame([items['id']],columns=['id'])\n",
    "        d = pd.concat([d,tempDF])\n",
    "d.to_csv('data/popularVideosList.csv', sep=',', encoding='utf-8')\n",
    "\n",
    "#Get a List of pupular video IDs\n",
    "d=pd.read_csv('data/popularVideosList.csv', index_col=0)\n",
    "list1=str(d[1:51]['id'].tolist())\n",
    "list1 = list1.replace(\" \",\"\")\n",
    "list1 = list1.replace(\"[\",\"\")\n",
    "list1 = list1.replace(\"]\",\"\")\n",
    "list1 = list1.replace(\"'\",\"\")\n",
    "list2=str(d[51:100]['id'].tolist())\n",
    "list2 = list2.replace(\" \",\"\")\n",
    "list2 = list2.replace(\"[\",\"\")\n",
    "list2 = list2.replace(\"]\",\"\")\n",
    "list2 = list2.replace(\"'\",\"\")\n",
    "\n",
    "d= pd.DataFrame()\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&maxResults=50&id=\"+list1+\"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data1=json.loads(r.text)\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&maxResults=50&id=\"+list2+\"&part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data2=json.loads(r.text)\n",
    "#'dislikeCount':[items['statistics']['dislikeCount']],'likeCount':[items['statistics']['likeCount']],\n",
    "for items in data1['items']:\n",
    "    tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'viewcount':[items['statistics']['viewCount']],'Published Date':[items['snippet']['publishedAt']]})\n",
    "    d = pd.concat([d,tempDF])\n",
    "for items in data2['items']:\n",
    "    tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'viewcount':[items['statistics']['viewCount']],'Published Date':[items['snippet']['publishedAt']]})\n",
    "    d = pd.concat([d,tempDF])\n",
    "d.to_csv('data/popularVideosCount.csv', sep=',', encoding='utf-8')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#Import Languges and Regions\n",
    "\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "import csv\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/i18nRegions?part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data = json.loads(r.text)\n",
    "d=pd.DataFrame()\n",
    "for items in data['items']:\n",
    "        tempDF=pd.DataFrame({'RegionID':[items['id']],'RegionName':[items['snippet']['name']]})\n",
    "        d = pd.concat([d,tempDF])\n",
    "d.to_csv('data/RegionCode.csv', sep=',', encoding='utf-8',index=False)\n",
    "\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/i18nLanguages?part=snippet&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data = json.loads(r.text)\n",
    "d=pd.DataFrame()\n",
    "for items in data['items']:\n",
    "        tempDF=pd.DataFrame({'LanguageID':[items['id']],'LanguageName':[items['snippet']['name']]})\n",
    "        d = pd.concat([d,tempDF])\n",
    "        #print(d)\n",
    "d.to_csv('data/LanguageCode.csv', sep=',', encoding='utf-8',index=False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Algeria\n",
      "39\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "'defaultAudioLanguage'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-48-2395d59491dc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     16\u001b[0m         \u001b[0mtitle\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'snippet'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'title'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mtitle\u001b[0m\u001b[1;33m!=\u001b[0m\u001b[1;34m'Deleted video'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m             \u001b[0mtempDF\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;34m'Title'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'snippet'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'title'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Country'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mix\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'RegionName'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Language'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'snippet'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'defaultAudioLanguage'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'CategoryId'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'snippet'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'categoryId'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'VideoID'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'id'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'ViewCount'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'statistics'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'viewCount'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'CountryCode'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mix\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'RegionID'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m             \u001b[0mdat\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconcat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdat\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtempDF\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'defaultAudioLanguage'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import math\n",
    "import time\n",
    "import requests\n",
    "d=pd.read_csv('data/RegionCode.csv')\n",
    "total=len(d)\n",
    "dat=pd.DataFrame()\n",
    "for i in d.index:\n",
    "    print(d.ix[i]['RegionName'])\n",
    "    r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&regionCode=\"+d.ix[i]['RegionID']+\"&chart=mostPopular&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "    data = json.loads(r.text)\n",
    "    nextPage=data['nextPageToken']\n",
    "    totalResults=math.floor(data['pageInfo']['totalResults']/5)-1\n",
    "    print(totalResults)\n",
    "    for items in data['items']:\n",
    "        title=items['snippet']['title']\n",
    "        if title!='Deleted video':\n",
    "            tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionName'],'CategoryId':[items['snippet']['categoryId']],'VideoID':[items['id']],'ViewCount':[items['statistics']['viewCount']],'CountryCode':d.ix[i]['RegionID']})\n",
    "            dat = pd.concat([dat,tempDF])\n",
    "          \n",
    "    for i in range(1,totalResults):\n",
    "        r = requests.get(\"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&regionCode=\"+d.ix[i]['RegionID']+\"&pageToken=\"+nextPage+\"&chart=mostPopular&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "        data = json.loads(r.text)\n",
    "        nextPage=data['nextPageToken']\n",
    "        for items in data['items']:\n",
    "            title=items['snippet']['title']\n",
    "            if title!='Deleted video':\n",
    "                tempDF=pd.DataFrame({'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionName'],'CategoryId':[items['snippet']['categoryId']],'VideoID':[items['id']],'ViewCount':[items['statistics']['viewCount']],'CountryCode':d.ix[i]['RegionID']})\n",
    "                dat = pd.concat([dat,tempDF])\n",
    "\n",
    "dat.to_csv('data/Data.csv', sep=',', encoding='utf-8',index=False)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'items'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-45-c786ee43df4a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=\"\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mix\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'RegionID'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;34m\"&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m     \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m     \u001b[1;32mfor\u001b[0m \u001b[0mitems\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'items'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m         \u001b[0mtempDF\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;34m'CategoryID'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'id'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Title'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'snippet'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'title'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Country'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mix\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'RegionID'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m         \u001b[0mdat\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconcat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdat\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtempDF\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'items'"
     ]
    }
   ],
   "source": [
    "#Import Categories for every country\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "d=pd.read_csv('data/RegionCode.csv')\n",
    "total=len(d)\n",
    "dat=pd.DataFrame()\n",
    "for i in d.index:\n",
    "    r = requests.get(\"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=\"+d.ix[i]['RegionID']+\"&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "    data = json.loads(r.text)\n",
    "    for items in data['items']:\n",
    "        tempDF=pd.DataFrame({'CategoryID':[items['id']],'Title':[items['snippet']['title']],'Country':d.ix[i]['RegionID']})\n",
    "        dat = pd.concat([dat,tempDF])\n",
    "dat.to_csv('data/VideoCategories.csv', sep=',', encoding='utf-8',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'nextPageToken'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-47-dbc8f4460f37>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mnextPage\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'nextPageToken'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0mcountry\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'regionCode'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0mtotalResults\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfloor\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'pageInfo'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'totalResults'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m/\u001b[0m\u001b[1;36m50\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'nextPageToken'"
     ]
    }
   ],
   "source": [
    "#Import all videos\n",
    "import pandas as pd\n",
    "import math\n",
    "import time\n",
    "dat=pd.DataFrame()\n",
    "r = requests.get(\"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "data = json.loads(r.text)\n",
    "nextPage=data['nextPageToken']\n",
    "country=data['regionCode']\n",
    "totalResults=math.floor(data['pageInfo']['totalResults']/50)-1\n",
    "print(totalResults)\n",
    "for items in data['items']:\n",
    "    title=items['snippet']['title']\n",
    "    if title!='Deleted video':\n",
    "        tempDF=pd.DataFrame({'Country':[country],'Title':[items['snippet']['title']],'Published At':[items['snippet']['publishedAt']],'VideoID':[items['id']['videoId']]})\n",
    "        dat = pd.concat([dat,tempDF])\n",
    "          \n",
    "for i in range(1,totalResults):\n",
    "    print(i)\n",
    "    r = requests.get(\"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&key=AIzaSyBVKyueCNHyygub0bupCWYRECDZMFmCCak\")\n",
    "    data = json.loads(r.text)\n",
    "    nextPage=data['nextPageToken']\n",
    "    print(nextPageToken)\n",
    "    country=data['regionCode']\n",
    "    for items in data['items']:\n",
    "        title=items['snippet']['title']\n",
    "        if title!='Deleted video':\n",
    "            tempDF=pd.DataFrame({'Country':[country],'Title':[items['snippet']['title']],'Published At':[items['snippet']['publishedAt']],'VideoID':[items['id']['videoId']]})\n",
    "            dat = pd.concat([dat,tempDF])\n",
    "\n",
    "dat.to_csv('data/AllVideos.csv', sep=',', encoding='utf-8',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\" seamless=\"seamless\" src=\"https://plot.ly/~mitali555/8.embed\" height=\"525px\" width=\"100%\"></iframe>"
      ],
      "text/plain": [
       "<plotly.tools.PlotlyDisplay object>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import plotly.plotly as py\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')\n",
    "for col in df.columns:\n",
    "    df[col] = df[col].astype(str)\n",
    "\n",
    "scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\\\n",
    "            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]\n",
    "\n",
    "df['text'] = df['state'] + '<br>' +\\\n",
    "    'Beef '+df['beef']+' Dairy '+df['dairy']+'<br>'+\\\n",
    "    'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+\\\n",
    "    'Wheat '+df['wheat']+' Corn '+df['corn']\n",
    "\n",
    "data = [ dict(\n",
    "        type='choropleth',\n",
    "        colorscale = scl,\n",
    "        autocolorscale = False,\n",
    "        locations = df['code'],\n",
    "        z = df['total exports'].astype(float),\n",
    "        locationmode = 'USA-states',\n",
    "        text = df['text'],\n",
    "        marker = dict(\n",
    "            line = dict (\n",
    "                color = 'rgb(255,255,255)',\n",
    "                width = 2\n",
    "            ) ),\n",
    "        colorbar = dict(\n",
    "            title = \"Millions USD\")\n",
    "        ) ]\n",
    "\n",
    "layout = dict(\n",
    "        title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',\n",
    "        geo = dict(\n",
    "            scope='usa',\n",
    "            projection=dict( type='albers usa' ),\n",
    "            showlakes = True,\n",
    "            lakecolor = 'rgb(255, 255, 255)'),\n",
    "             )\n",
    "    \n",
    "fig = dict( data=data, layout=layout )\n",
    "py.iplot( fig, filename='d3-cloropleth-map' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
