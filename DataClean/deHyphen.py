import os

target = open("list.txt","r")

targetlist = target.readlines()
fixlist = []
count = 0
target.close()

for i in targetlist:
    fixlist.append(i[:-1])
    fixlist[count]= fixlist[count][0:2]+fixlist[count][3:7]+fixlist[count][8:10]
    fixlist[count]= fixlist[count].upper()
    print fixlist[count]
    count = count+1

rename = open("noHyphen.txt","w")

for item in fixlist:
    rename.write(item+"\n")

rename.close()

leave = input("\nEnter for Leave")
