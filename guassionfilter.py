import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("image is not found")
#apllying gaussion filter to the image
img2=cv.GaussianBlur(img,(5,5),0)
cv.imshow("original image",img)
cv.imshow("Gausssion filter image",img2)
cv.waitKey(0)
cv.destroyAllWindows()


