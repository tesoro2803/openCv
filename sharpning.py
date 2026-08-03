import cv2 as cv
import numpy as np
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("image is not found")
#imput the kernal matrix of image
kernal=np.array([[-1, -1, -1],
 [-1,  9, -1],
 [-1, -1, -1]])
#applying filter to the image
sharp=cv.filter2D(img,-1,kernal)
cv.imshow("original image",img)
cv.imshow("fil  tered image",sharp)
cv.waitKey(0)
cv.destoryAllWindows()
