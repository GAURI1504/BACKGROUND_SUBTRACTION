# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:14:19 2021

@author: gauri
"""

import cv2
video_capture = cv2.VideoCapture(0)
i=1
while(i>0):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if i<5:
        background=frame    
    sub=cv2.subtract(frame,background)
    # Display the resulting frame
    cv2.imshow('Video', sub)
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the ca
video_capture.release()
cv2.destroyAllWindows()