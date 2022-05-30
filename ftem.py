from PIL import Image
import colorsys

#which gun is it?
gun="elderflame"
#which variant to?

#Function for all guns -> Variants (WIP)
def pink_blastx(x,y,z):
    temp=(x,y,z)
    #pink
    if(x<345/360) and (x>310/360):
        if(y>0.1) and (z+y>0.8):
            temp=((x+30/360)%1,y,z)
    #purple
    elif(x<310/360) and (x>240/360):
        if(y>0.1) and (z+y>0.75):
            temp=((x+90/360)%1,y,z)
    #cyan
    elif(x<190/360) and (x>145/360):
        if(z+y>0.5) and (y>0.1):
            temp=((x)%1,y,z)
    #blue
    elif(x<240/360) and (x>175/360):
        if(z+y>0.5) and (y>0.3):
            temp=((x-35/360)%1,y,z)
    return temp

def ion(x,y,z):
    temp=(x,y,z)
    if(180/360<x) and (x<280/360) and (y+z>1):
        temp=((x+0.15)%1,y,z)
    return temp

def yellow_prime(x,y,z):
    temp=(x,y,z)
    if(x>40/360) and (x<70/360):
        if(y+z>0.7):
            temp=((x+0.2)%1,y,z)
    return temp

def gaia_red(x,y,z):
    temp=(x,y,z)
    if(x<10/360) or (x>340/360):
        if(y+z>1.1):
            temp=((x+0.5)%1,y,z)
    return temp

def elderflame(x,y,z):
    temp=(x,y,z)
    if(x>180/360) and (x<280/360):
        if(y+z>0.75):
            temp=((x+0.77)%1,y,z)
    return temp

#definitive gun function
if(gun=="pink_blastx"):
    def wgun(x,y,z):
        return pink_blastx(x,y,z)
elif(gun=="ion"):
    def wgun(x,y,z):
        return ion(x,y,z)
elif(gun=="yellow_prime"):
    def wgun(x,y,z):
        return yellow_prime(x,y,z)
elif(gun=="gaia_red"):
    def wgun(x,y,z):
        return gaia_red(x,y,z)
elif(gun=="elderflame"):
    def wgun(x,y,z):
        return elderflame(x,y,z)

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
        (i,j)=(mask[index])
        #read rgb and convert to hsv
        (r,g,b)=(pixels[i,j])
        hsv=colorsys.rgb_to_hsv(r/255,g/255,b/255)
        (h,s,v)=(hsv)
        #Edit
        (h,s,v)=wgun(h,s,v)
        #apply edit
        rgb=colorsys.hsv_to_rgb(h,s,v)
        r=int(255*rgb[0])
        g=int(255*rgb[1])
        b=int(255*rgb[2])
        pixels[i,j]=(r,g,b)

    im.save(outfilename)
