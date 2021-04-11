# -*- coding: utf-8 -*-
"""
The purpose of this programme is to crawl datas about newest movies from DouBan

By Hongjie Fan

"""
from hw1_crawler import get
from tkinter import *
import tkinter.messagebox as messagebox

movielist="" #a string to store movies names and their score

class Application(Frame): #gui
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.Label = Label(self, text='   click the button below you will see the newest movies and their scores   \n')
        self.Label.pack()
        self.Button = Button(self, text='Check', command=self.data)
        self.Button.pack()
        self.Labe2 = Label(self, text='\n data from Douban © Hongjie Fan')
        self.Labe2.pack()
        
    def data(self):
        messagebox.showinfo('A list of movies for your reference', movielist)

lists=get('https://movie.douban.com/cinema/nowplaying/hefei/')

for s in lists:
    movielist=movielist+s  #combine all elements in movielist into one strin
    
app = Application()
app.master.title('picking moive assistant')
app.mainloop()
