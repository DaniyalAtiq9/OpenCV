import cv2 as cv
# Reading an image
img = cv.imread("Photos\cat.jpg")

cv.imshow("Cat", img)

cv.waitKey(5000)
# Reading a video
# capture = cv.VideoCapture("Videos\dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Dog", frame)
#     if cv.waitKey(20) & 0xFF ==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()