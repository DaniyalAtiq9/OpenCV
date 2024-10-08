import cv2 as cv
import numpy as np

img = cv.imread('Photos\park.jpg')

# Image Translation
# def translation(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)

# -x --> Left
# -y --> Up
# x  --> Right
# y  --> Down

# translated = translation(img,100,100)
# cv.imshow('Translated', translated)

# Rotating an Image
# def rotate(img, angle, rotpoint=None):
#     (height, width) = img.shape[:2]
#     if rotpoint is None:
#         rotpoint = (width//2, height//2)
#     rotMatrix = cv.getRotationMatrix2D(rotpoint,angle,scale=1.0)
#     dimensions = (width, height)
#     return cv.warpAffine(img,rotMatrix,dimensions)

# rotated = rotate(img,270)
# cv.imshow('Rotated', rotated)


# Flipping an image
flip = cv.flip(img, -1)
# cv.imshow("Original", img)
cv.imshow('Flipped', flip)


cv.waitKey(0)