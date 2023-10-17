'''import cv2 as cv

capture = cv.VideoCapture('vid.mp4')

while True:
    istrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    capture.release()
    cv.destroyAllWindows() 
'''


import cv2 as cv

capture = cv.VideoCapture('vid.mp4')

while True:
    is_true, frame = capture.read()

    # Check if the frame was read successfully
    if not is_true:
        break

    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the capture object and close all windows
capture.release()
cv.destroyAllWindows()
