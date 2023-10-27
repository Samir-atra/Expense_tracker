import cv2 as cv
from datetime import datetime
import os

def capture():
# a function to capture a photo and save it with the title as the current time
    path = os.getcwd()
    cam = cv.VideoCapture(0)   
    while (True):
        _, frame = cam.read()
        cv.imshow('image', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        title = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    cv.imwrite(f"{path}/Images/images/{title}.jpg",frame)
    cv.destroyWindow("cam-test")
    return True

if __name__ == "__main__":
    capture()