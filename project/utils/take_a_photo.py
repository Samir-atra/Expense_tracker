import cv2 as cv


x = 1
cam = cv.VideoCapture(0)   
# s, img = cam.read()
while x == 1:
    ret, frame = cam.read()
    cv.imshow('frame', frame)
    cv.waitKey(0)
    x = input("what is x")
    # cv.destroyWindow("cam-test")
    # cv.imwrite("filename.jpg",img)