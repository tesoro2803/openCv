import cv2 as cv
img=cv.imread(r"S:\CV\123.jpg")
#image is not found then raise error
if img is None:
    raise ValueError("jpg is not found") 
#apllying brightness to the image  
bright=cv.convertScaleAbs(img, alpha=1.5, beta=50)
cv.imshow("Original Image", img)
cv.imshow("Bright Image", bright)
cv.waitKey(0)
cv.destroyAllWindows()