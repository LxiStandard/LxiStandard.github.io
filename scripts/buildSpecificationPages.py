#!python

# This program creates the LXI specification pages from the
# root directory specificationsIN which is pushed to the repo
# when a change is made to the specifications repo

import os

# directories
specificationsIN="specificationsIN"
specificationsOUT="site/specifications"
versionInfoFilename="VersionInfo.md"

defaultVersionInfo="""---
layout: default
title: Temporary Specifications Version
nav_order:  1
---

Please Create a VersionInfo.md file in the LxiStandard:specifications repository
with descriptive information about this specification set.

"""

# this class holds a line item for the URL table
filenameRE= r""
class documentInfo(filename):
    rawURL=""
    sortKey=""
    name=""
    date=""
    version=""
    URLdocx=""
    URLpdf=""
    URLhtml=""




# called from root directory where spec version resides
def getVersionInfo(): 
    content=defaultVersionInfo
    if os.path.isfile(versionInfoFilename):
        with open(versionInfoFilename,'r') as file:
            content=file.read()
    # extra newline so markdown doesn't flow together
    content += "\n"
    return content

# called from root directory where spec version resides
def buildURLTable():
    fileList=[]
    files= os.listdir()
    for file in files:
        fileList.add(parseFilename(file))
    fileList.sort(lambda:x x.sortKey)


# start by cleaning out the old specifications directory
#os.removedirs(specificationsOUT)
#os.mkdir(specificationsOUT)


# Get a list of the directories, each represents a different specification set

rootDir=os.curdir
os.chdir(specificationsIN)
specSets=os.listdir()


for directory in specSets:
    os.chdir(specificationsIN+"/"+dir)
    versionInfoMarkdown=getVersionInfo()

    versionInfoMarkdown+=buildURLTable()

    



