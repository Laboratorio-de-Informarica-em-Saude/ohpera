import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    gray = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY),5)
    circles=cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 10)
    if circles!=None:
        print "Circle There !"

        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:

            cv2.circle(gray, (x, y), r, (0, 255, 0), 4)
    cv2.imshow('video',gray)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
