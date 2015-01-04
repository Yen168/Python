import os

f = open("dejpg.txt")
w = open("dejpg_fin.txt","w")
deal = f.readlines()
f.close()

for item in deal:
    item = item[0:2]+item[3:7]+item[8:10]
    w.write(item+"\n")

w.close()
