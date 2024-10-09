import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
# cv.imshow('Image', img)

# blank
blank = np.zeros(img.shape,dtype='uint8')
# cv.imshow("Blank", blank)

# grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# blur
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

# canny edge
canny = cv.Canny(blur,125,175)
cv.imshow("Canny", canny)

# threshold --> binarizes image
# only takes grayscaled image...
# ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("Threshold", thresh)

# use canny method first and then try to find contours rather than threshold the image
# contours
contours, heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

# draw contours
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours drawn', blank)


cv.waitKey(0)