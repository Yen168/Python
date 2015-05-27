import os

desc = os.getcwd()
catalogList = []
catalogPrice="2014.11.10"

print "Get file list..."

for root, dirs, files in os.walk(desc):
    for f in files:
        #print os.path.join(root, f)
        guest = f.split(".")[-1]
        if guest.upper()in ["JPG","JPEG"]:
            if f not in catalogList:
                catalogList.append(f)

listNum = len(catalogList)

print "Making catalog..."

newhtml = open("catalog_test.html","w")
newhtml.write('''<html><head><title>My Test</title></head><body>''')
count = 0

def catalogHtml(tr,td):
    #count = 0
    global count
    newhtml.write('''<h1 align = "center">Company</h1><br><br><table>''')
    for r in range(tr):
        newhtml.write('''<tr>''')
        for d in range(td):
            if count < listNum:
                newhtml.write('''<td><img src="'''+catalogList[count]+'''" alt="'''+catalogList[count]+'''" height="240" width="240"><p align = "center"><b>'''+catalogList[count][0:7].replace("_","-")+" "+catalogList[count][8:10]+'''</b></p></td>''')
                count = count + 1
            else:
                newhtml.write('''<td></td>''')
                #newhtml.write("")
            
        newhtml.write('''</tr>''')

    newhtml.write('''</table><br><h2 align = "center">TEL: |  | FAX: </h2><br><br><br><br></body></html>''')

    if listNum > count:
        catalogHtml(tr,td)
    else:
        newhtml.close()

print "Starting add list..."
catalogHtml(5,5)
print "Finished..."
