import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("Image not found")
#aplying thresholding to the image
ret, thresh=cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
cv.imshow("original imsge",img)
cv.imshow("threshold image",thresh)
cv.waitKey(0)
cv.destroyAllWindows()
