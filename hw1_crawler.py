# -*- coding: utf-8 -*-
"""
The purpose of this programme is to crawl datas about newest movies from DouBan

By Hongjie Fan

"""

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error

findName=re.compile(r'<img alt="(.*?)" class="" rel="nofollow"',re.S)
findScore=re.compile(r'data-score="(.*?)" data-showed=',re.S)

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    request = urllib.request.Request(url,headers = head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('li',class_="list-item"):
        item = str(item)
        name = re.findall(findName,item)
        score = re.findall(findScore,item)
        if len(score)==0 :
            score.append("no score by now")
        print(name[0],score[0])

