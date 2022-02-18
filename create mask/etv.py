import cv2
import numpy as np
import os

print("Converting Frames to Video")
img=[]
i=0
name='mask_'+str(i)+'.png'
while(os.path.exists(name)):
    img.append(cv2.imread(name))
    i+=1
    name='mask_'+str(i)+'.png'

count=i
height,width,layers=img[1].shape

video=cv2.VideoWriter('resultmask.mp4',-1,60,(width,height))

for j in range(0,count):
    video.write(img[j])

cv2.destroyAllWindows()
video.release()

print("Done")
