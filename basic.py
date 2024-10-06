import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT) # you can increase blur intensity by increasing the kernel values
# Try putting even values for kernel
# cv.imshow('Blurr', blur)

# Edge Cascade
canny = cv.Canny(blur,125,175)
# cv.imshow("Canny", canny)

# Dilation
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow("Dilate", dilated)

# Erosion
eroded = cv.erode(dilated,(7,7), iterations=3)
# cv.imshow("Erode", eroded)

# Resizing
resized = cv.resize(img,(500,500)) # using default interpolation, you can use other
# try cv.INTER_CUBIC
cv.imshow("Resized", resized)

# Cropping
cropped = img[20:200, 200:400]
cv.imshow("Cropped", cropped)




cv.waitKey(0)