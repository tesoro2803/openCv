# import the CV package
import cv2 as cv
# read the image using imread()function
img=cv.imread(r"S:\CV\1234.jpeg")
# Check if the image was loaded or not
if img is None:
    print("jpg is not found")
else:
    # display the image
    cv.imshow("image", img)
    # wait until a key is pressed
    cv.waitKey(0)