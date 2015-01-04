import os
import shutil

nowdir= os.getcwd()
dstdir= "C:\Documents and Settings\Scan\Desktop\_COPY_nojpeg"
notinlist=[]
copyname=''
storename=''

if not os.path.exists(dstdir):
    os.makedirs(dstdir)

target = open("searchlist.txt","r")
targetlist = target.readlines()
fixlist = []

for i in targetlist:
    fixlist.append(i[:-5])
   

target.close()

for dirPath, dirNames, fileNames in os.walk(nowdir):
    for f in fileNames:
        for itemname in fixlist:
            if itemname.replace("_","-").upper() == f[0:10].replace("_","-").upper():
                print os.path.join(dirPath, f)
                copyname=os.path.join(dirPath, f)
                shutil.copy(copyname, dstdir)

leave = input("\nEnter for Leave")
