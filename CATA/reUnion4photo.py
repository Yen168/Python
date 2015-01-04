import os
import shutil

nowdir= os.getcwd()
copyname=''
storename=''
countCopy=0

disdir = "C:\\Documents and Settings\\Scan\\Desktop\\reUnion"
os.makedirs(disdir)

for dirPath, dirNames, fileNames in os.walk(nowdir):
    for f in fileNames:
        if (f[-3:].upper() == "JPG") and not (os.path.exists(disdir+"\\"+f[0:2])):
            os.makedirs(disdir+"\\"+f[0:2])
            copyname=os.path.join(dirPath, f)
            shutil.copy(copyname, disdir+"\\"+f[0:2])
            print "copy.."+copyname
            countCopy = countCopy+1
        elif f[-3:].upper() == "JPG":
            copyname=os.path.join(dirPath, f)
            shutil.copy(copyname, disdir+"\\"+f[0:2])
            print "copy.."+copyname
            countCopy = countCopy+1
        

    #for f in fileNames:
        #copyname=os.path.join(dirPath, f)
        #shutil.copy(copyname, nowdir+"\\"+f[0:2])
        #countCopy = countCopy+1
        

print countCopy
leave = input("\nEnter for Leave")

# use first 2 letter of file name to group photo
