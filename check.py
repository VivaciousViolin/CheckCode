
import os
import sys
from tkinter import Tk


from tkinter.filedialog import askdirectory
folderpath = askdirectory(title='select folder to scan') # shows dialog box and return the path
print(folderpath)  
    
filelist = os.listdir(folderpath)
print(filelist)

"""
def searchpath(path):
    f = open(path, "r")
    print(f.read())

searchpath(path)
"""