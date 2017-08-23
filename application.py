import Tkinter as tk
from tkFileDialog import askopenfilename
from skeletonEstimation import run

# Global variable
counter = 0

def openfile():
   filename = askopenfilename(parent=root)
   lblText.config(text=filename)
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
lblText = tk.Label(root, text = "test")
lblText.pack()
btnBrowse = tk.Button(root, text="Browse", command = openfile)
btnBrowse.pack(side = tk.LEFT, padx=5, pady = 5)
btnKeyframe = tk.Button(root, text="Keyframe")
btnKeyframe.pack(side = tk.LEFT, padx=5, pady = 5)
btnExport = tk.Button(root, text="Export")
btnExport.pack(side = tk.LEFT, padx=5, pady = 5)
btnAbout = tk.Button(root, text="About", command = openAbout)
btnAbout.pack(side = tk.RIGHT, padx=5, pady = 5)
root.mainloop()