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
import os
import numpy as np
from math import ceil

from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)

#example address: ".\me.jpg"
class interestingImageFilter():
    
    PIL_GRAYSCALE = 'L'
    PIL_WIDTH_INDEX = 0
    PIL_HEIGHT_INDEX = 1
    COMMON_MONO_FONT_FILENAMES = [
        'DejaVuSansMono.ttf',  # Linux
        'Consolas Mono.ttf',   # MacOS
        'Consola.ttf',         # Windows
    ]
    outputName="demo"
    
    
    txtOutputScaling_X = 3 #The higher the less pixels
    txtOutputScaling_Y = 9 #The higher the less pixels
    
    currentFilter = []
    CharFilter0 = [',','1','2','3','4','s','w','#','$','@']
    CharFilter1 = CharFilter0[::-1]
    CharFilter2 = [x for x in range(0,10)]
    def setFilterMode(self, i=0):
        if i == 0:
            self.currentFilter = self.CharFilter0
        if i == 1:
            self.currentFilter = self.CharFilter1
        if i == 2:
            self.currentFilter = self.CharFilter2
                
    def __init__(self, imageAddress):
        self.img = io.imread(imageAddress)
        self.setFilterMode()
        
    def printImgDimensions(self):
        print("height: ", len(self.img), ", width: ", len(self.img[0]),", RGB: ", len(self.img[0][0]))
    
    def printBlurImg(self):
        """Blurring Image"""
        sigma = 3.0
        # apply Gaussian blur, creating a new image
        blurred = skimage.filters.gaussian(
            self.img, sigma=(sigma, sigma), truncate=3.5, multichannel=True)
        #print("height: ", len(blurred), ", width: ", len(blurred[0]))
        plt.imshow(blurred)
        plt.show()
        
    def writeNumTxt(self):
        """Scale down image"""
        image_resized = resize(self.img, (self.img.shape[0] // self.txtOutputScaling_Y, self.img.shape[1] // self.txtOutputScaling_X), anti_aliasing=True)
        """Grayscaling image"""
        #grayscale formula: ( (0.3 * R) + (0.59 * G) + (0.11 * B) )
        height = len(image_resized)
        width = len(image_resized[0])
        """write to file"""
        f = open(self.outputName+'.txt', "a")
        f.truncate(0)
        for i in range(height):
            row = []
            for j in range(width):
                temp = image_resized[i][j][0]*255*0.3+image_resized[i][j][1]*255*0.59+image_resized[i][j][2]*255*0.11
                image_resized[i][j] = temp
                row.append(self.currentFilter[int(temp//25)])
            f.write(''.join(str(e) for e in row))
            f.write('\n')
        f.close()
        
    def getNumTxt(self):
        """This will return a text file that contains image in number form"""
        self.writeNumTxt()
        os.startfile(self.outputName+'.txt')
        
    def getNumImg(self):
        """This will return a jpg file that contains image in number form"""
        self.writeNumTxt()
        image = self.textfile_to_image(self.outputName+'.txt')
        image.save(self.outputName+'.jpg')
        os.startfile(self.outputName+'.jpg')
        
    def textfile_to_image(self, textfile_path):
        """Convert text file to a grayscale image.
    
        arguments:
        textfile_path - the content of this file will be converted to an image
        font_path - path to a font file (for example impact.ttf)
        """
        # parse the file into lines stripped of whitespace on the right side
        with open(textfile_path) as f:
            lines = tuple(line.rstrip() for line in f.readlines())
    
        # choose a font (you can see more detail in the linked library on github)
        font = None
        large_font = 20  # get better resolution with larger size
        for font_filename in self.COMMON_MONO_FONT_FILENAMES:
            try:
                font = ImageFont.truetype(font_filename, size=large_font)
                print(f'Using font "{font_filename}".')
                break
            except IOError:
                print(f'Could not load font "{font_filename}".')
        if font is None:
            font = ImageFont.load_default()
            print('Using default font.')
    
        # make a sufficiently sized background image based on the combination of font and lines
        font_points_to_pixels = lambda pt: round(pt * 96.0 / 72)
        margin_pixels = 20
    
        # height of the background image
        tallest_line = max(lines, key=lambda line: font.getsize(line)[self.PIL_HEIGHT_INDEX])
        max_line_height = font_points_to_pixels(font.getsize(tallest_line)[self.PIL_HEIGHT_INDEX])
        realistic_line_height = max_line_height * 0.8  # apparently it measures a lot of space above visible content
        image_height = int(ceil(realistic_line_height * len(lines) + 2 * margin_pixels))
    
        # width of the background image
        widest_line = max(lines, key=lambda s: font.getsize(s)[self.PIL_WIDTH_INDEX])
        max_line_width = font_points_to_pixels(font.getsize(widest_line)[self.PIL_WIDTH_INDEX])
        image_width = int(ceil(max_line_width + (2 * margin_pixels)))
    
        # draw the background
        background_color = 255  # white
        image = Image.new(self.PIL_GRAYSCALE, (image_width, image_height), color=background_color)
        draw = ImageDraw.Draw(image)
    
        # draw each line of text
        font_color = 0  # black
        horizontal_position = margin_pixels
        for i, line in enumerate(lines):
            vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
            draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)
    
        return image
            
    def printImg(self):
        io.imshow(self.img)



iif = interestingImageFilter(".\\ny.jpg")
iif.setFilterMode(0)
iif.getNumImg()
