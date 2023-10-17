import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/navee/Desktop/sikandar/Coding/Python/OpenCV/melonoma.jpeg')
#cv.imshow('Flower',img)

# translation of image
def translate(img,x,y):
    trans_mat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1], img.shape[0])
    shifted=cv.warpAffine(img,trans_mat,dimensions)
    return shifted

 # -ve value for x and +ve y values to move left or right respectively
 # -x --> Left
 # -y --> up
 # x --> right
 # y --> down

translated= translate(img,100,100)
cv.imshow('translate',translated)

# Rotation of Image
def rotate (image , angle ):
    rows,cols,ch = image.shape
    center =( cols// 2 ,rows // 2 )
    M = cv.getRotationMatrix2D((center),angle,1)#rotation matrix
    rotatedImage = cv.warpAffine(image,M,(cols,rows))
    return rotatedImage


rotatedImg =rotate(img,-45)
cv.imshow('Rotate',rotatedImg)

rotated_rotated= rotate(rotatedImg,-45)
cv.imshow("Rotated Rotate",rotated_rotated)


# Flipping
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Cropping
cropped = img[50:100, 180:200]
cv.imshow('Cropped', cropped)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
cv.waitKey(0)