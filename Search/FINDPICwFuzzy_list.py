import os
import shutil

nowdir= os.getcwd()
dstdir= "C:\Documents and Settings\Scan\Desktop\_sku_rt_o1"
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

#print fixlist
#print fuzzyList

#clean list
#print fuzzyList
#for i in fuzzyList:
    #for j in fixlist:
        #if i[0:7] == j[0:7]:
            #if i in fuzzyList:
                #fuzzyList.remove(i)

finalList = list(fuzzyList)

if len(fuzzyList) != 0:
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
                    #print copyname
                    #print changename
                    #shutil.copy(copyname, dstdir)
                    shutil.copy(copyname, changename)
                    fuzzyCount = fuzzyCount+1
                    if itemname in finalList:
                        finalList.remove(itemname)

    print "Found.. "+str(fuzzyCount)


if len(finalList)!=0:
    print "Item count not be found..."
    print finalList

else:
    print "ALL FOUND!"

nofoundtarget = open("nofoundlist.txt","w")

for item in finalList:
    nofoundtarget.write(item+"\n")

nofoundtarget.close()

leave = input("\nEnter for Leave")
