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

#example address: ".\me.jpg"
class interestingImageFilter():
    def __init__(self, imageAddress):
        self.img = io.imread(imageAddress)
    def printImgDimensions(self):
        print("height: ", len(self.img), ", width: ", len(self.img[0]),", RGB: ", len(self.img[0][0]))
    
    
    def printblurImg(self):
        """Blurring Image"""
        sigma = 3.0
        # apply Gaussian blur, creating a new image
        blurred = skimage.filters.gaussian(
            self.img, sigma=(sigma, sigma), truncate=3.5, multichannel=True)
        #print("height: ", len(blurred), ", width: ", len(blurred[0]))
        plt.imshow(blurred)
        plt.show()
    def getNumImg(self):
        """Scale down image"""
        yScaling = 6
        xScaling = 1
        image_resized = resize(self.img, (self.img.shape[0] // yScaling, self.img.shape[1] // xScaling),
                               anti_aliasing=True)
        #print("Resized: height: ", len(image_resized), ", width: ", len(image_resized[0]), ", rgb: ", image_resized[0][0])
        """Grayscaling image"""
        #grayscale formula: ( (0.3 * R) + (0.59 * G) + (0.11 * B) )
        height = len(image_resized)
        width = len(image_resized[0])
        """write to file"""
        f = open("demo.txt", "a")
        f.truncate(0)
        for i in range(height):
            row = []
            for j in range(width):
                temp = image_resized[i][j][0]*255*0.3+image_resized[i][j][1]*255*0.59+image_resized[i][j][2]*255*0.11
                image_resized[i][j] = temp
                row.append(int(temp//25))
            f.write(''.join(str(e) for e in row))
            f.write('\n')
        f.close()
    def printImg(self):
        io.imshow(self.img)



iif = interestingImageFilter(".\me.jpg")
iif.printImg()
