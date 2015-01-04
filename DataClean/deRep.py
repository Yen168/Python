import os

f = open("rep.txt","r")
deal = f.readlines()
f.close()

newlist = []
countlist = {}

for item in deal:
    if item[:-1] not in newlist:
        newlist.append(item[:-1])
        countlist[item[:-1]]=1
    else:
        countlist[item[:-1]]=countlist[item[:-1]]+1

#for item in newlist:
#    print item

fw = open("result_static.txt","w")

for k, v in sorted(countlist.iteritems()):
    #print k, v
    fw.write(k+" "+str(v)+"\n")

fw.close()

#print os.stat("ff.jpg")
print "the other thing:"
count_list = 0

for k, v in sorted(countlist.iteritems()):

    if int(v) >1:
        print k, v
        count_list = count_list+1
    else:
        count_list = count_list+1

print count_list
