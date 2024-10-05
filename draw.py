import cv2 as cv
import numpy as np

# Creating a blank image with numpy
# uint8 is basically datatype of an image
blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

# This selects all indexes in the numpy array
# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# numpy array indexing
# (height, width, channels)
# 200:300 refers to the height(number of rows) and 300:400 refers to the width(number of columns)
# 0,0,255 is the color depth which is 3 as specified in blank declaration
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red2', blank)

# Drawing a rectangle
# This takes an image, initial coordinates, ending coordinates, color and thickness of the rectangle
# cv.rectangle(blank, (250,250), (500,500), (255,0,0), thickness=cv.FILLED) # try thickness = 2, -1
# Instead of (250,250), try (blank.shape[1]//2,blank.shape[0]//2)
# cv.imshow('Rectangled', blank)

# Drawing a circle
# Once you know how to draw a rectangle, circle is easy
# cv.circle(blank, (250,250),40, (0,0,255),thickness=3)
# cv.imshow('Circled', blank)
# Play around with it

# Drawing a line
# cv.line(blank, (250,250), (500,500), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# Writing text
cv.putText(blank,"Text",(250,250),cv.FONT_HERSHEY_PLAIN,2.0,(255,255,255),thickness=3) # Try entering a longer sentence
# If the text goes off screen, try to adjust the origin margins (No other way to handle it)
cv.imshow("Text", blank)
cv.waitKey(0)