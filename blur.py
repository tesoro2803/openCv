import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("Image not found")
#applying average filter to the image
filter1=cv.blur(img,(5,5))
cv.imshow("original image",img)
cv.imshow("blurred image",filter1)
cv.waitKey(0)
cv.destroyAllWindows()
