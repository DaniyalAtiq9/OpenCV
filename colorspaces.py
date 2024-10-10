import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/Park.jpg')
# cv.imshow('Image', img)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV -> BGR', hsv_bgr)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB", lab)

# L*A*B to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow("LAB -> BGR", lab_bgr)

# OpenCV reads images as BGR images, however, it's not the format applied everywhere
# as RGB format is more commonly used, to demonstrate this let's try to display
# an image via matplotlib
# plt.imshow(img)
# plt.show()
# The matplotlib's default format is RGB, therefore you can notice the color inversion 
# of the image as compared to when you displayed it via opencv

# We can convert BGR to RGB as well
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)
# And when you pass this rgb to matplotlib the color inversion will not happen
# plt.imshow(rgb)
# plt.show()

# Reverse this process
rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
# cv.imshow('RGB -> BGR', rgb_bgr)

# Note that to convert a grayscale image to any other format, there is no direct method
# so you have to first convert that image back to BGR and then you can do that.
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# you would need to reconvert it back into bgr before you could apply format conversion
# this is becaue grayscale image has a single channel, while color spaces like HSV
# and LAB expect a 3-channel images like BGR




cv.waitKey(0)