# -*- coding: utf-8 -*-
"""
The purpose of this programme is to crawl datas about newest movies from DouBan

By Hongjie Fan

"""
from hw1_crawler import get
from tkinter import *
import tkinter.messagebox as messagebox

movielist=""

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.Label = Label(self, text='click the button below you can see the newest movies and their score')
        self.Label.pack()
        self.alertButton = Button(self, text='Check', command=self.data)
        self.alertButton.pack()
        self.Labe2 = Label(self, text='data from Douban © Hongjie Fan')
        self.Labe2.pack()
        
    def data(self):
        messagebox.showinfo('movie list', movielist)

lists=get('https://movie.douban.com/cinema/nowplaying/hefei/')
for s in lists:
    movielist=movielist+s
app = Application()
# 设置窗口标题:
app.master.title('movies')
# 主消息循环:
app.mainloop()