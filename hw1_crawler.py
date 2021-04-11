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

class movies(object):
    
    def __init__(self, item):
        self.name = re.findall(findName,item)
        self.score = re.findall(findScore,item)
        if len(self.score)==0: #this condition means there no score by now
            self.score.append("no score by now")
        if self.score[0]=='0': #this is anothor condition meaned no score
            self.score[0]="no score by now"
        
    def combinedata(self):
        return self.name[0]+" "+self.score[0]+"\n"

def get(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    request = urllib.request.Request(url,headers = head)
    response = urllib.request.urlopen(request)
    html = response.read()
    htmltext=BeautifulSoup(html,"html.parser")
    movielist=[] # a list stored movies' name and score
    for item in htmltext.find_all('li',class_="list-item"):
        item = str(item)
        movie=movies(item)
        movielist.append(movie.combinedata()) 
    return movielist
