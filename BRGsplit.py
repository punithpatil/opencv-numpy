import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
#height, width, depth
while(1):

    # Take each frame
    _, frame = cap.read()

    
    height, width, depth = frame.shape
    #print height, width, depth
    #print frame[..., 0]
    z = np.zeros((height, width), frame.dtype)
    #f = np.array((frame[..., 0], z, z), frame.dtype)
    b, g, r = cv2.split(frame)
    
    cv2.imshow('blue', cv2.merge([frame[..., 0], z, z]))
    cv2.imshow('green', cv2.merge([z, g,z]))#np.array((z, frame[..., 1], z)))
    cv2.imshow('red', cv2.merge([z, z, r]))#np.array((z, z,frame[..., 2])))
   
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
