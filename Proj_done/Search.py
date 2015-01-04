import os
import shutil

nowdir= "F:\Macintosh\ALL PICTURES\ORIGINAL #1 (catalog)"
dstdir= os.getcwd()+'''\\result'''
fuzzy_needs ='Y'

print "Search folder: " + nowdir
print "Result in folder: " + dstdir
print "Will you need fuzzy search? "
fuzzy_needs = raw_input("Your Choice (Y/N) : ")

copyname=''
storename=''
countCopy=0
fuzzyCount = 0
fuzzyList = []

if not os.path.exists(dstdir):
    os.makedirs(dstdir)

target = open("searchlist.txt","r")
targetlist = target.readlines()
fixlist = []

for i in targetlist:
    fixlist.append(i[:-1])

target.close()

fuzzyList = list(fixlist)

for dirPath, dirNames, fileNames in os.walk(nowdir):
    for f in fileNames:
        for itemname in fixlist:
            if itemname.replace("_","-").upper() == f[0:10].replace("_","-").upper():
                print os.path.join(dirPath, f)
                copyname=os.path.join(dirPath, f)
                shutil.copy(copyname, dstdir)
                countCopy = countCopy+1
                if itemname in fuzzyList:
                    fuzzyList.remove(itemname)


print "Found.. "+str(countCopy)


finalList = list(fuzzyList)

if len(fuzzyList) != 0 and fuzzy_needs.upper()=='Y':
    print "Fuzzy Search for..."
    print fuzzyList
    print "Starting Fuzzy Search..."
    for dirPath, dirNames, fileNames in os.walk(nowdir):
        for f in fileNames:
            for itemname in fuzzyList:
                if itemname[0:7].replace("_","-").upper() == f[0:7].replace("_","-").upper():
                    print os.path.join(dirPath, f)
                    copyname=os.path.join(dirPath, f)
                    changename = os.path.join(dstdir, f[0:-4]+"_fuzzy_"+itemname[8:10]+".jpg")
                    
                    shutil.copy(copyname, changename)
                    fuzzyCount = fuzzyCount+1
                    if itemname in finalList:
                        finalList.remove(itemname)

    print "Found.. "+str(fuzzyCount)


if len(finalList)!=0:
    print "Item count not be found..."
    print finalList

    nofoundtarget = open("nofoundlist.txt","w")

    for item in finalList:
        nofoundtarget.write(item+"\n")

    nofoundtarget.close()

else:
    print "ALL FOUND!"


leave = raw_input("\nEnter for Leave")
