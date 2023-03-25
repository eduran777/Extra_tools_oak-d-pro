import cv2

import os


in_path = '/Users/usuario/Documents/Frames/Frames interpolacion/1-1944301041BBED1200-left/'

out_path = '/Users/usuario/Documents/Frames/Frames interpolacion/routeClip3fps/'

out_video_name = 'Clip6.mp4'

out_video_full_path = out_path + out_video_name

preimg = os.listdir(in_path)


preimg.sort()
del preimg[0]
#print(preimg)


img = []

for i in preimg:

    i = in_path + i

    img.append(i)

print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
print(img[0])
print('/Users/usuario/Documents/Frames/Prubas 03-03-2032/Left/1-18443010C176631200-5fps/Video1-1-18443010C176631200-left-5fps01939.png')

size = list((192,1000,4))

del size[2]



print(size)


video = cv2.VideoWriter(out_video_full_path,cv2_fourcc,3,size) #output video name, fourcc, fps, size

for i in range(len(img)):

    video.write(cv2.imread(img[i]))

video.release()

