import cv2 as cv
import matplotlib.pyplot as plt

#img = cv.resize(cv.imread('C:/Users/navee/Desktop/sikandar/Coding/Python/OpenCV/pimple.jpg'), (500,600), interpolation=cv.INTER_CUBIC)
img = cv.imread('C:/Users/navee/Desktop/sikandar/Coding/Python/OpenCV/melonoma.jpeg')
cv.imshow('Image', img)

rgb=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('RGB',rgb)

plt.imshow(img)
plt.show()
#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert to grayscale
cv.imshow('Gray',gray)

# HSV
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)# convert to hsv colorspace
cv.imshow("HSV",hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)  ## Convert image from RGB to Lab Color Space
cv.imshow("Lab", lab)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)
cv.waitKey(0)