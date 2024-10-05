import numpy as np
import cv2

n=50
img=np.zeros((n*8,n*8,3),dtype=np.uint8)
for row in range(8):
    for col in range(8):
        if (row+col)%2==0:
            img[row*n:(row+1)*n,col*n:(col+1)*n]=255,255,255
cv2.imshow('8*8checkerboard',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
                
