import PIL
import os
from PIL import Image


print "Photo Resize"

for filename in os.listdir("."):
    
    if filename[-3:].upper() == "JPG":

        print "processing... "+ filename
        outfile = filename[:-4] + "_300.jpg"
        # setting
        basewidth = 1200
        img = Image.open(filename)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        # higt quality resize: ANTIALIAS
        img.save(outfile)
        print "Result: " +outfile+ " ...done!"

# batch resize photo
