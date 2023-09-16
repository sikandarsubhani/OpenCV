import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

'''
# paint image with color of choice
blank[:]=0,255,0
cv.imshow('Green',blank)

#color the custom pixels range
blank[100:200, 300:400]=0,0,255
cv.imshow('red',blank)
''' 
#draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255), thickness=3)
#fill the rectangle with color
cv.rectangle(blank,(0,0),(250,250),(0,0,255), thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(250,250),(0,0,255), thickness=-1)

#rectangle to Square
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,255), thickness=3)
cv.circle(blank, (45,45), 40, (0,255,0), thickness=-1)
cv.imshow("Rectangle", blank)

# draw a line 
cv.line(blank, (100,100), (200,100), (255,255,0),thickness=3)
cv.imshow("Line", blank)

#write text on an image 



cv.putText(blank,'Hello',(300,300),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,255),2)
cv.imshow("Text", blank)
cv.waitKey(0)