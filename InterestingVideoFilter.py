# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:14:49 2022

@author: Haowei Li
"""
# importing the necessary libraries
import cv2
import numpy as np
class InterestingVideoFilter():
    
    def __init__(self, video):
    # Creating a VideoCapture object to read the video
        self.cap = cv2.VideoCapture(video)
     
    def blackAndWhite1(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
         
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                                 interpolation = cv2.INTER_CUBIC)
         
            # Display the resulting frame
            cv2.imshow('Frame', frame)
         
            # conversion of BGR to grayscale is necessary to apply this operation
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
            # adaptive thresholding to use different threshold
            # values on different regions of the frame.
            Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                   cv2.THRESH_BINARY_INV, 11, 2)
         
            cv2.imshow('Thresh', Thresh)
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
         
        # release the video capture object
        self.cap.release()
        # Closes all the windows currently opened.
        cv2.destroyAllWindows()
    
    def blackAndWhite2(self):
        
        height = 540
        width = 380
        # Loop until the end of the video
        while (self.cap.isOpened()):
            
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (height, width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            
            # conversion of BGR to grayscale is necessary to apply this operation
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            """
            for i in range(len(frame)):
                for j in range(len(frame[0])):
                    frame[i][j] = np.dot(frame[i][j], [0.3, 0.59, 0.11])
            cv2.imshow('Thresh', frame)        """
            
            
            #print(type(frame[0][0]))
            # adaptive thresholding to use different threshold
            # values on different regions of the frame.
         
            
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            
            
    def smoothing(self):
        # Loop until the end of the video
        height = 540
        width = 380
        while (self.cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (height, width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            
            # using cv2.Gaussianblur() method to blur the video
            
            # (5, 5) is the kernel size for blurring.
            gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0)
            cv2.imshow('gblur', gaussianblur)
         
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    def cv2Testing(self):
         
        # creating a square of zeros using a variable
        rectangle = np.zeros((300, 300), dtype="uint8")
        cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
        cv2.imshow("Rectangle", rectangle)
            
        # creating a circle of zeros using a variable
        circle = np.zeros((300, 300), dtype="uint8")
        cv2.circle(circle, (150, 150), 150, 255, -1)
        cv2.imshow("Circle", circle)
            
        bitwiseAnd = cv2.bitwise_and(rectangle, circle)
        cv2.imshow("AND", bitwiseAnd)
        
        while True:
            k = cv2.waitKey(100) 
            if k==27: 
                print('ESC')
                cv2.destroyAllWindows()
                break        
            if (cv2.getWindowProperty('Rectangle',cv2.WND_PROP_VISIBLE) < 1 or
            cv2.getWindowProperty('Circle',cv2.WND_PROP_VISIBLE) < 1 or
            cv2.getWindowProperty('AND',cv2.WND_PROP_VISIBLE) < 1):
                cv2.destroyAllWindows()
                break  
        
iv = InterestingVideoFilter('video.mp4')
iv.cv2Testing()