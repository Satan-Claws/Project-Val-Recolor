import cv2
print("Reading Frames")
vidcap = cv2.VideoCapture('vid.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("xx_frame%d.png" % count, image)    
  count += 1
  success,image = vidcap.read()
  

f=open("cons.txt","a")
f.write(str(count))
f.close()

print("Frames extracted, Frame Count: ", count)
