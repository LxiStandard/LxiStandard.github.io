#!python

# This program creates the LXI specification pages from the
# root directory specificationsIN which is pushed to the repo
# when a change is made to the specifications repo

import os
import re
import sys
import shutil



# directories
specificationsIN=r"specificationsIN"
specificationsOUT=r"site/specifications"
versionInfoFilename="VersionInfo.md"

defaultVersionInfo="""---
layout: default
title: Temporary Specifications Version
parent: Specifications
nav_order:  1
---

Please Create a VersionInfo.md file in the LxiStandard:specifications repository
with descriptive information about this specification set.

"""

# this class holds a line item for the URL table
class documentInfo:
    rawURL=""
    sortKey=""
    name=""
    date=""
    version=""
    URLdocx=""
    URLpdf=""
    URLhtml=""

    def __init__(self, filename):
        filenameRE= r"([\w\d-]+)_(\d+\.\d+)_(\d\d\d\d-\d\d-\d\d).(.*)"
        match= re.match(filenameRE,filename)
        if (match):
            self.name = match.group(1)
            self.version= match.group(2)
            self.date= match.group(3)
            self.suffix= match.group(4)
            if self.suffix.upper()=="PDF":
                self.URLpdf=filename
            elif (self.suffix.upper()=="DOC") | (self.suffix.upper()=="DOCX"):
                self.URLdocx=filename
            elif (self.suffix.upper()=="HTM") | (self.suffix.upper()=="HTML"):
                self.URLhtml=filename
            else:
                self.rawURL=filename
                self.sortKey=filename
            self.sortKey=self.name+self.date
        else:
            self.rawURL=filename
            self.name=filename
            self.sortKey=filename
        
    
    # returns true if items were mergeable and updates self to merged
    def merge(self, addend):
        if (self.rawURL != "") | (addend.rawURL != ""):
            return 
        if (self.name == addend.name) & (self.version == addend.version) & (self.date == addend.date):
            # same identity just different file so merge
            if self.URLdocx=="":
                self.URLdocx= addend.URLdocx
            if self.URLhtml=="":
                self.URLhtml= addend.URLhtml
            if self.URLpdf=="":
                self.URLpdf= addend.URLpdf
            return 
         
    # create the markdown table line for this instance
    def markdown(self):
        md = ""
        if self.rawURL == "":
            md = self.name + "|" + self.version + "|" + self.date + "|" 
            if self.URLdocx != "":
                md += "[docx](" + self.URLdocx + ")|"
            else:
                md += "-|"
            if self.URLpdf != "":
                md += "[pdf](" + self.URLpdf + ")"
            else:
                md += "-"
            # Skip HTML for now
        else:
            md = self.rawURL + "||||"
        return md  




# called from root directory where spec version resides
def buildURLTable(directory):
    fileList=dict()
    files= os.listdir(directory)
    for file in files:
        fileInfo = documentInfo(file)
        if fileInfo.sortKey in fileList:
            fileList[fileInfo.sortKey].merge(fileInfo)
        else:
            fileList[fileInfo.sortKey] = fileInfo
    lines= list(fileList.keys())
    lines.sort()
    output= []
    output.append("|Title|Ver|Date|Word|PDF|")
    output.append("|---|:---:|---|:---:|:---:|")
    for line in lines:
        newItem = fileList[line]
        output.append(newItem.markdown())
    return output

# called from root directory where input spec version resides
def writeVersionInfo(directoryName, toRoot, specTable): 

    # get header from default above or input file
    content=defaultVersionInfo
    inputFile=directoryName+r"/"+versionInfoFilename
    if os.path.isfile(inputFile):
        with open(inputFile,'r') as file:
            content=file.read()
    # extra newline so markdown doesn't flow together
    content += "\n"

    #write the VersionInfo.md file with appended table
    versionFile = toRoot+r"/"+directoryName+r"/"+versionInfoFilename
    if os.path.isfile(versionFile):
        os.remove(versionFile)
    file= open(versionFile, "w+") 
    file.write(content)
    for line in specTable:
        file.write(line)
        file.write("\n")
    file.close





# start by cleaning out the old specifications directory
#os.removedirs(specificationsOUT)
#os.mkdir(specificationsOUT)


# Get a list of the directories, each represents a different specification set

# entirely rewrite specification output directory, so delete old and create anew
if os.path.isdir(specificationsOUT):
    shutil.rmtree(specificationsOUT, ignore_errors=True)
shutil.copytree(specificationsIN, specificationsOUT)

# build the tables
os.chdir(specificationsIN)
specSets=os.listdir()
for directory in specSets:
    table = buildURLTable(directory)
    writeVersionInfo(directory,"../"+specificationsOUT, table)
    

    



