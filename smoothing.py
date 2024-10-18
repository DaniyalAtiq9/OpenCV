import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow("Image", img)

# Image blurring or smoothing is a process that makes the image less sharp and reduces its level of detail.
# There are 4 types of image smoothing:
# 1. Averaging 2. Gaussian Blurring 3. Median Blurring 4. Bilateral Blurring

# 1. Averaging
averaged = cv.blur(img, (3,3))
# The kernel(must be an odd-matrix) is 3x3 filter that will compute the pixel intensity of the 
# middle pixel (true center) and average it based on the surrounding pixels. Increasing the kernel
# size will increase the blur.
# Suppose a 3x3 kernel is:
# | 1 1 1 |                                  | 1 1 1 |
# | 1 1 1 | then averaging will work as:  1\9| 1 1 1 |
# | 1 1 1 |                                  | 1 1 1 |
# This kernel window slides through the whole image averaging each pixel value.
cv.imshow("Averaged", averaged)

# 2. Gaussian Blurring
gauss = cv.GaussianBlur(img, (3,3), 0) # 0 is standard deviation(sigma) for x direction, if sigma for y is not explicitly mentioned, the value of sigma x is taken as default
# Unlike Avearging, Gaussian method assigns particular weights to each surrounding pixel. The average
# of the products of the weights give the value of true center. This method gives less blurring than
# Averaging method but it is more natural.
cv.imshow("Gaussian Blur", gauss)

# 3. Median Blurring
median = cv.medianBlur(img, 3)
# Except for finding the average of the surrounding pixels, it finds the median of the surrounding pixels.
# More effective in reducing noise as compared to Averaging, and, Gaussian Blurring. It is very good at
# removing salt and pepper noise.
# Notice that in the function an integer 3 is passed instead of a tuple, this is because opencv automatically
# assumes that the kernel size will be 3 x 3 based on the integer value.
cv.imshow("Median Blurring", median)
# MedianBlur() uses a single integer because it inherently operates on square kernels, while other methods like
# GaussianBlur() require more control over the dimensions(must be positive and odd),
# however can vary, hence the tuple.

# 4. Bilateral Filtering
# Other methods simply blur the image and have no concern with the edges in the image. Bilateral Blurring
# blurs the image and retains the edges in that image. Bilateral filtering also takes a Gaussian filter
# in space, but one more Gaussian filter which is a function of pixel difference. The Gaussian function
# of space makes sure that only nearby pixels are considered for blurring, while the Gaussian function
# of intensity difference makes sure that only those pixels with similar intensities to the central
# pixel are considered for blurring. So it preserves the edges since pixels at edges will have large
# intensity variation. It is however slower compared to other functions.
bilateral = cv.bilateralFilter(img,3,15,15) # 3 is the Diameter of pixel neighborhood and 15 is the sigma
                                            # color which means more colors in the neighborhood will be
                                            # considered when applying the blur. 15 Sigma space means
                                            # that pixels further out from the central pixel will influence blur.
cv.imshow("Bilateral Blurring", bilateral)

# Play around with the parameter values and compare the differences between each method.
cv.waitKey(0)