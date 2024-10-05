import cv2 as cv
# Rescaling an image
# img = cv.imread('Photos\cat.jpg')
# cv.imshow("Cat", img)

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_img = rescale_frame(img)
# cv.imshow("Resized Cat", resized_img)
# cv.waitKey(0)

# Rescaling a video
capture = cv.VideoCapture('Videos\dog.mp4')
while True:
    isTrue, frame = capture.read()
    resized_frame = rescale_frame(frame)
    cv.imshow('Original Video', frame)
    cv.imshow('Resized Video', resized_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()