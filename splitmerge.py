import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')
cv.imshow("Park", img)
# print(img.shape)
# Splitting the bgr image into three color channels
b,g,r = cv.split(img)
# Display the image
# cv.imshow("Blue",b)
# cv.imshow("Green",g)
# cv.imshow("Red",r)
# Compare the color channels
# print(b.shape)
# print(g.shape)
# print(r.shape)
# You will notice that the images being displayed are grayscale images.
# The shape of split images is (427,640) whereas, the original image
# has a shape of (427,640,3). This is because the original image is
# a BGR image with 3 color channels. The split images are grayscale 
# images which have only one color channel which is not explicitly
# shown in here (427,640). The split images show color intensity 
# distribution. For example, in the image 'b', the sky has light
# intensity showcasing that the color blue is present in great
# intesity here, while other parts of the image have dark
# intensity meaning that the color blue is not present here. The
# case remains the same for red and green images as well.

# Merging the image
merged = cv.merge([b,g,r]) # Pass in a list of color channels
# cv.imshow("Merged", merged)
# Merging the image converts it back into the bgr image

# For clarity let's merge the color channels of the bgr
# image with the help of blank image.
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("Blue Blank", blue)
cv.imshow("Green Blank", green)
cv.imshow("Red Blank", red)
print(blue.shape)
# Now notice instead of a grayscale image we have 
# a 3 channel image which sets the other colors
# to blank(which is just a black image) and it 
# shows the distribution of the color intensity.
# Remember: Lighter area represents higher density of that color and vice versa.




cv.waitKey(0)