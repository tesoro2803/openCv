import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("Image not found")
#applying reflection to the image
reflection=cv.flip(img,1)
cv.imshow("original image",img)
cv.imshow("Reflection image",reflection)
cv.waitKey(0)
cv.destroyAllWindows()