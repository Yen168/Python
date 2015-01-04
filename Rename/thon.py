import os

f=open("createjpg.txt","r")
makelis = f.readlines()

for f in makelis:
    lis = f[:-1]+".jpg"
    fw = open(lis,"w")
    fw.close()

# make empty jpg
