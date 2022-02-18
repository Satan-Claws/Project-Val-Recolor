from PIL import Image
import colorsys

f=open("cons.txt","r")
xx=f.readlines()
count=int(xx[0])
f.close()

imask=Image.open("mask.png")
pix=imask.load()
w,h=imask.size
for no in range(0,count):
    print(no)
    inpfilename="xx_frame"+str(no)+".png"
    im=Image.open(inpfilename)
    pixels=im.load()
    width,height=im.size
    for i in range(width//3,width):
        for j in range(0,height):
            temp_1=0
            r=pixels[i,j][0]
            g=pixels[i,j][1]
            b=pixels[i,j][2]
            hsv=colorsys.rgb_to_hsv(r/255,g/255,b/255)
            h=hsv[0]
            s=hsv[1]
            v=hsv[2]
            lower=165
            upper=230
            if(h>lower/360) and (h<upper/360):
                temp_1=1
            if(temp_1==1) and (s+v>1): pix[i,j]=(0,0,0)
    imask.save("mask_"+str(no)+".png")
