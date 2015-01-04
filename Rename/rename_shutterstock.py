import os

for filename in os.listdir("."):
    print filename
    if filename.startswith("shutterstock_"):
        os.rename(filename, filename[:-4]+"GEM"+".JPG")
