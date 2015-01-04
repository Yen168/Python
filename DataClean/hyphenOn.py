import os

target = open("needHyphen.txt","r")

targetlist = target.readlines()
fixlist = []
count = 0
target.close()

for i in targetlist:
    fixlist.append(i[:-1])
    fixlist[count]= fixlist[count][0:2]+"-"+fixlist[count][2:6]+"-"+fixlist[count][6:8]
    fixlist[count]= fixlist[count].upper()
    print fixlist[count]
    count = count+1

rename = open("hyphenOn.txt","w")

for item in fixlist:
    rename.write(item+"\n")

rename.close()

leave = input("\nEnter for Leave")
