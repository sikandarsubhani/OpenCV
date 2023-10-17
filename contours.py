import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/navee/Desktop/sikandar/Coding/Python/OpenCV/melonoma.jpeg')
cv.imshow('Melonoma', img)

blank = np.zeros(img.shape,'uint8')
#gray
gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray_image)

# Blur
blur = cv.GaussianBlur(gray_image,(5,5),cv.BORDER_DEFAULT) # (kernel size , sigmaX,sigmaY)
cv.imshow("Blurred Image", blur)

# canny Edges
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)