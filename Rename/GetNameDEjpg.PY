import os

w = open("dejpg_fin.txt","w")
nowdir = os.getcwd()
finish = []

for dirPath, dirNames, fileNames in os.walk(nowdir):
    for f in fileNames:
        if (f[-3:].upper() == "JPG") and f not in finish:
            print f
            finish.append(f)
            w.write(f[0:2]+f[3:7]+f[8:10]+"\n")
        

w.close()
