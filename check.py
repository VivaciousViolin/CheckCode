
import os
import sys
from tkinter import Tk


from tkinter.filedialog import askdirectory
folderpath = askdirectory(title='select folder to scan') # shows dialog box and return the path
print(folderpath)  

extensions = [".txt", ".py", ".bat"]

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


subfolders, files = run_fast_scandir(folderpath, extensions)
for x in subfolders:
    print(x + "   ---   this is a subfolder")
for x in files:
    print(x + "   ---   this is a subfolder")

"""
#grabs the folder and all of the subfolders
def find_dirs(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(find_dirs(dirname))
    return subfolders #yoinked and modified from https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory

def find_file_names(dirname):

folders = find_dirs(folderpath)
print(folders)


#filelist = os.listdir(folderpath)
#print(filelist)
"""
"""
def searchpath(path):
    f = open(path, "r")
    print(f.read())

searchpath(path)
"""