# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:40:26 2022

@author: Haowei Li
"""
from skimage import io
from skimage.util import img_as_ubyte



img = io.imread(".\me.jpg")
print("height: ", len(img), ", width: ", len(img[0]),", RGB: ", len(img[0][0]))

highest = 0
lowest = 255
#greyscale formula: ( (0.3 * R) + (0.59 * G) + (0.11 * B) )
height = len(img)
width = len(img[0])
number_pic = []
for i in range(height):
    row = []
    for j in range(width):
        temp = img[i][j][0]*0.3+img[i][j][1]*0.59+img[i][j][2]*0.11
        img[i][j] = temp
        row.append(int(temp//25))
    number_pic.append(row)
    

#write to file
f = open("demo.txt", "a")
for i in range(len(number_pic)):
    #print(''.join(number_pic[i]))
    #print(number_pic[i]) 
    f.write(''.join(str(e) for e in number_pic[i]))

f.close()
io.imshow(img)

# =============================================================================
# #save image
# img = img_as_ubyte(img)
# io.imsave(".\gray.jpg", img)
# 
# =============================================================================
