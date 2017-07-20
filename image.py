# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:23:45 2017

@author: tungnb
"""

from PIL import Image, ImageTk
import Tkinter
from Tkinter import *

root = Tkinter.Tk()
im = PhotoImage(file="res/about.gif")
tim = im.subsample(50,50)


btnBrowse = Tkinter.Button(root, text="Browse")
btnBrowse.config(image = tim, compound = TOP)
btnBrowse.pack(side = Tkinter.LEFT, padx=5, pady = 5)
root.mainloop()