import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('sample.jpg')
cv.imshow('original', img)
resizedImg = rescaleFrame(img,0.1)
cv.imshow('resized', resizedImg)

cv.waitKey()