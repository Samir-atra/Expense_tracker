import cv2 as cv
from datetime import datetime

def capture():

    cam = cv.VideoCapture(0)   
    # s, img = cam.read()
    now = datetime.now()
    while (True):
        ret, frame = cam.read()
        cv.imshow('image', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        # x = input("what is x")
        title = now.strftime("%d-%m-%Y %H-%M-%S")
        cv.imwrite(f"/home/samer/Desktop/Beedoo/Expenses_tracker/project/utils/Images/{title}.jpg",frame)
        cv.destroyWindow("cam-test")
    return True

if __name__ == "__main__":
    capture()