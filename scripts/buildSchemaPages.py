# Requires Python 3 or greater.

# This program creates the LXI schema pages from the
# root directory schemasIN which is pushed to the repo
# when a change is made to the lxi-api repo

import os
import re
import sys
import shutil



# directories
schemasIN=r"schemasIN/"
schemasOUT=r"site/schemas/"
schemaInfoFilename="SchemaInfo.md"

defaultSchemaInfo="""---
layout: default
title: Temporary schema information
parent: Schemas
nav_order:  1
---

Please Create a SchemaInfo.md file in the LxiStandard:lxi-api repository
with descriptive information about this schema.

"""


# General flow
#  copy everything wholesale to the schemas directory
#  for every directory
#     for each xsd file 
#        scrape editorial date
#     rename .xsd file without suffix.
#     make the table of versions (Editorial Date, Version, Doc)
#     add table of versions onto the SchemaInfo.md file
#     


# fix the filename of the version and create the table for schema info

def stripSuffixAndBuildTable(specName):
    schemasFiles=[]
    xmlFiles=[]
    directory=specName+"/"
    for file in os.listdir(directory ):
        if file.endswith(".xsd"):
            schemasFiles.append(file)
        elif file.endswith(".xml"):
            xmlFiles.append(file)
    
    table=[]
    table.append("")
    table.append("## Schemas")
    table.append("")
    #table.append("|---|---|---|")
    table.append("| |Version|Doc")
    for file in schemasFiles:
        shortname = file[:-4]
        os.rename(directory+file, directory+shortname)
        linkSchema = "["+shortname+"]"+"("+shortname+")"
        linkDoc="None"
        if os.path.isfile(directory+shortname+".html"):
            linkDoc="[doc]"+"("+shortname+".html"+")"
        table.append(specName+"|"+linkSchema+"|"+linkDoc)
    
    table.append("")

    # Add in example links
    if len(xmlFiles)!=0:
        table.append("## Examples")
        table.append("")
        for example in xmlFiles:
            table.append("  * ["+example+"]("+example+")")
        table.append("")

    return table
    




def updateSchemaInfo(directory, versionTable):
     # get header from default above or input file
    header=defaultSchemaInfo
    summaryMdFile=directory+r"/"+schemaInfoFilename

    if os.path.isfile(summaryMdFile):
        with open(summaryMdFile,'r') as file:
            header=file.read()
        os.remove(summaryMdFile)       # just recreate new file below

    #write the SchemaInfo.md file
    file= open(summaryMdFile, "w+") 
    file.write(header)
    file.write("\n")     # make sure header doesn't flow into table
    for line in versionTable:
        file.write(line +  "\n")
    file.close
    return


# entirely rewrite schema output directory, so delete old and create anew
if os.path.isdir(schemasOUT):
    shutil.rmtree(schemasOUT, ignore_errors=True)
shutil.copytree(schemasIN, schemasOUT)


# build the tables
os.chdir(schemasOUT)
schemas=os.listdir()
for directory in schemas:
    versionTable=stripSuffixAndBuildTable(directory)
    updateSchemaInfo(directory, versionTable)
