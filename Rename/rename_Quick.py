import os

for filename in os.listdir("."):
    if filename[-3:].upper() == "JPG":
        os.rename(filename,filename.replace("-","_"))
