import cv2 as cv


img = cv.resize(cv.imread('C:/Users/navee/Desktop/sikandar/Coding/Python/OpenCV/trace.jpg'), (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Trace', img)
#gray
gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray_image)

# Canny Edges
canny=cv.Canny(img,125,175) 
cv.imshow("Edges", canny)

# Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
cv.waitKey(0)