import cv2 as cv
#read image using imread() funtion
img=cv.imread(r"S:\CV\1234.jpeg")
#image is not found then raise error
if  img is None:
    raise ValueError("Image not found")
#find thwe height and width of image
(h,w)=img.shape[:2]
#find the center of the image
center=(w//2,h//2)
#create the rotation matrix
matrix=cv.getRotationMatrix2D(center,45,1.0)
#rotate the image using warpAffine() function
rotated=cv.warpAffine(img,matrix,(w,h))
cv.imshow("original image",img)
cv.imshow("rotated image",rotated)
cv.waitKey(0)
cv.destroyAllWindows()