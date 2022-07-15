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
     
    def blackAndWhite(self):
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
    
    def blackAndWhite(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
         
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
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
            
            
    def smoothing(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            print(frame)
            
            # using cv2.Gaussianblur() method to blur the video
         
            # (5, 5) is the kernel size for blurring.
            gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0)
            cv2.imshow('gblur', gaussianblur)
         
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
iv = InterestingVideoFilter('video.mp4')
iv.blackAndWhite()