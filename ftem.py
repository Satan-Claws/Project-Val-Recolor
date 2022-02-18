from PIL import Image
import colorsys

#functions
def between(h,lo,up):
    if(h>lo/360) and (h<up/360):
        return 1
    else:
        return 0
#which gun is it?

#read how many frames to edit
f=open("cons.txt","r")
xx=f.readlines()
count=int(xx[0])   #number of frames
f.close() 

#read mask
print("Reading Mask")
mask=[]   #pixels over which to edit
maskc=0   #number of pixels

imask=Image.open("mask.png")
pixx=imask.load()
w,h=imask.size
for i in range(0,w):
    for j in range(0,h):
        if(pixx[i,j]==(0,0,0)):
            mask.append([i,j])
            maskc+=1

print("Mask loaded")

#edit each image
for no in range(0,count):
    print("Editing Frame:",no,100*no/count,"%")
    inpfilename="xx_frame"+str(no)+".png"
    outfilename="xx_result"+str(no)+".png"
    im=Image.open(inpfilename)
    pixels=im.load()
    width,height=im.size
    for index in range(0,maskc):
        i=mask[index][0]
        j=mask[index][1]

        #read rgb and convert to hsv
        r=pixels[i,j][0]
        g=pixels[i,j][1]
        b=pixels[i,j][2]
        hsv=colorsys.rgb_to_hsv(r/255,g/255,b/255)
        h=hsv[0]
        s=hsv[1]
        v=hsv[2]
        #Edit
        #pink
        pink=0
        if(h<345/360) and (h>310/360) and (s+v>0.8) and (v>0.1):
            pink=1
        #purple
        purple=0
        if(h<310/360) and (h>240/360) and (s+v>0.75) and (v>0.1):
            purple=1
        #cyan
        cyan=0
        if(h<190/360) and (h>145/360) and (s+v>0.5) and (v>0.1):
            cyan=1
        #blue
        blue=0
        if(h<240/360) and (h>175/360) and (s+v>0.5) and (v>0.3):
            blue=1
        #change
        sh=no/120
        if(pink==1):
            (h,s,v)=(h,0,(1+v)/2)
        elif(purple==1):
            (h,s,v)=((h+sh+0.25)%1,s,v)
        elif(cyan==1):
            (h,s,v)=((h+sh+0.5)%1,s,v)
        elif(blue==1):
            (h,s,v)=((h+sh+0.4)%1,s,v)

        #apply edit
        rgb=colorsys.hsv_to_rgb(h,s,v)
        r=int(255*rgb[0])
        g=int(255*rgb[1])
        b=int(255*rgb[2])
        pixels[i,j]=(r,g,b)

    im.save(outfilename)
