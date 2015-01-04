import PIL
import os
from PIL import Image
import ImageDraw, ImageFont


print "Photo Resize"

for filename in os.listdir("."):
    
    if filename[-3:].upper() == "JPG":

        print "processing... "+ filename
        outfile = filename[:-4] + "_300.jpg"
        
        basewidth = 300
        img = Image.open(filename)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('TIMES.ttf',30)
        
        print "Name: " +filename[0:10].replace("_","-").upper()+ " ..."
        draw.ink = 0 + 0*256 + 0*256*256
        draw.text((75,(hsize-30)), filename[0:7].replace("_","-").upper()+" "+filename[8:10].upper(),font = font)
        img.save(outfile)
        print "Result: " +outfile+ " ...done!"


