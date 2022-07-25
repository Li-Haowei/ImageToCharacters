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
        self.height = 540
        self.width = 380
     
    def blackAndWhite1(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
         
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (self.height, self.width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
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
        # Loop until the end of the video
        while (self.cap.isOpened()):
            
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (self.height, self.width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            
            im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Frame1', im_gray)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            
    def blackAndWhite3(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
         
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (self.height, self.width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                                 interpolation = cv2.INTER_CUBIC)
         
            # Display the resulting frame
            cv2.imshow('Frame', frame)
         
            
            im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(im_gray, thresh=120, maxval=255, type=cv2.THRESH_BINARY)
            im_thresh_gray = cv2.bitwise_and(im_gray, mask)
            cv2.imshow('Thresh', im_thresh_gray)
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
         
        # release the video capture object
        self.cap.release()
        # Closes all the windows currently opened.
        cv2.destroyAllWindows()     
        
    def smoothing(self):
        while (self.cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (self.height, self.width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
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
        # the bitwise_and function executes the AND operation
        # on both the images
        bitwiseAnd = cv2.bitwise_and(rectangle, circle)
        cv2.imshow("AND", bitwiseAnd)
        
        # the bitwise_or function executes the OR operation
        # on both the images
        bitwiseOr = cv2.bitwise_or(rectangle, circle)
        cv2.imshow("OR", bitwiseOr)
        
        # the bitwise_xor function executes the XOR operation
        # on both the images
        bitwiseXor = cv2.bitwise_xor(rectangle, circle)
        cv2.imshow("XOR", bitwiseXor)
        
        # the bitwise_not function executes the NOT operation
        # on both the images
        bitwiseNot = cv2.bitwise_not(rectangle, circle)
        cv2.imshow("NOT", bitwiseNot)
                   
        while True:
            k = cv2.waitKey(100) 
            if k==27: 
                print('ESC')
                cv2.destroyAllWindows()
                break        
            if (cv2.getWindowProperty('Rectangle',cv2.WND_PROP_VISIBLE) < 1 or
                cv2.getWindowProperty('Circle',cv2.WND_PROP_VISIBLE) < 1 or
                cv2.getWindowProperty('AND',cv2.WND_PROP_VISIBLE) < 1 or
                cv2.getWindowProperty('XOR',cv2.WND_PROP_VISIBLE) < 1 or
                cv2.getWindowProperty('NOT',cv2.WND_PROP_VISIBLE) < 1 or
                cv2.getWindowProperty('OR',cv2.WND_PROP_VISIBLE) < 1):
                cv2.destroyAllWindows()
                break  

        
    def mangaLiked(self):
        # Loop until the end of the video
        while (self.cap.isOpened()):
         
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            try:
                frame = cv2.resize(frame, (self.height, self.width), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            except:
                # release the video capture object
                self.cap.release()
                # Closes all the windows currently opened.
                cv2.destroyAllWindows()
                break
            frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                                 interpolation = cv2.INTER_CUBIC)
         
            # Display the resulting frame
            cv2.imshow('Frame', frame)
         
            
            im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(im_gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
            #im_thresh_gray = cv2.bitwise_and(im_gray, mask)
            #cv2.imshow('im_thresh_gray', im_thresh_gray)
        
            
            mask3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) 
            im_thresh_color = cv2.bitwise_and(frame, mask3)
            cv2.imshow('im_thresh_color', im_thresh_color)
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
         
        # release the video capture object
        self.cap.release()
        # Closes all the windows currently opened.
        cv2.destroyAllWindows()
iv = InterestingVideoFilter('video.mp4')
iv.mangaLiked()