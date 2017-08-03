import Tkinter as tk
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
from test2 import run

# Global variable
counter = 0

def openfile():
   filename = askopenfilename(parent=root)   
   if len(filename) != 0:
       print filename
       run(filename)
   
def openAbout():
    global counter
    counter += 1
    t = tk.Toplevel()
    t.wm_title("Window #%s" % counter)
    l = tk.Label(t, text="This is window #%s" % counter)
    l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

# Main
root = tk.Tk()
root.wm_title("Hello, world")

# Make image button
imBrowse = PhotoImage(file="res/browse.gif")
timBrowse = imBrowse.subsample(5,5)
imKey = PhotoImage(file="res/key.gif")
timKey = imKey.subsample(5,5)
imExport = PhotoImage(file="res/export.gif")
timExport = imExport.subsample(5,5)
imAbout = PhotoImage(file="res/about.gif")
timAbout = imAbout.subsample(5,5)


btnBrowse = tk.Button(root, text="Browse", command = openfile)
btnBrowse.config(image = timBrowse, compound = TOP)
btnBrowse.pack(side = tk.LEFT, padx=5, pady = 5)
btnKeyframe = tk.Button(root, text="Keyframe")
btnKeyframe.config(image = timKey, compound = TOP)
btnKeyframe.pack(side = tk.LEFT, padx=5, pady = 5)
btnExport = tk.Button(root, text="Export")
btnExport.config(image = timExport, compound = TOP)
btnExport.pack(side = tk.LEFT, padx=5, pady = 5)
btnAbout = tk.Button(root, text="About", command = openAbout)
btnAbout.config(image = timAbout, compound = TOP)
btnAbout.pack(side = tk.RIGHT, padx=5, pady = 5)
root.mainloop()