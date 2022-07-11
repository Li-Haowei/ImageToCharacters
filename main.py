# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:40:26 2022

@author: Haowei Li
"""
from skimage import io, data, color
from skimage.util import img_as_ubyte
import skimage.filters
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread(".\me.jpg")
print("height: ", len(img), ", width: ", len(img[0]),", RGB: ", len(img[0][0]))

# =============================================================================
# """Blurring Image"""
# sigma = 3.0
# # apply Gaussian blur, creating a new image
# blurred = skimage.filters.gaussian(
#     img, sigma=(sigma, sigma), truncate=3.5, multichannel=True)
# print("height: ", len(blurred), ", width: ", len(blurred[0]))
# plt.imshow(blurred)
# plt.show()
# =============================================================================

"""Scale down image"""
image_resized = resize(img, (img.shape[0] // 4, img.shape[1] // 1),
                       anti_aliasing=True)
print("Resized: height: ", len(image_resized), ", width: ", len(image_resized[0]), ", rgb: ", image_resized[0][0])
"""Grayscaling image"""
#grayscale formula: ( (0.3 * R) + (0.59 * G) + (0.11 * B) )
height = len(image_resized)
width = len(image_resized[0])
number_pic = []
for i in range(height):
    row = []
    for j in range(width):
        temp = image_resized[i][j][0]*255*0.3+image_resized[i][j][1]*255*0.59+image_resized[i][j][2]*255*0.11
        image_resized[i][j] = temp
        row.append(int(temp//25))
    number_pic.append(row)


"""write to file"""
f = open("demo.txt", "a")
f.truncate(0)
for i in range(len(number_pic)):
    #print(''.join(number_pic[i]))
    #print(number_pic[i]) 
    f.write(''.join(str(e) for e in number_pic[i]))
    f.write('\n')

f.close()
#io.imshow(img)

# =============================================================================
# #save image
# img = img_as_ubyte(img)
# io.imsave(".\gray.jpg", img)
# 
# =============================================================================
