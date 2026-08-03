import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if img is None:
    raise ValueError("Image not found")
#applying scaling to the image
scaled = cv.resize(img, None, fx=2, fy=2)
cv.imshow("original image",img)
cv.imshow("Scaled", scaled)
cv.waitKey(0)
cv.destroyAllWindows()