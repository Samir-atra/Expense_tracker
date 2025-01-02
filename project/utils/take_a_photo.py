"""
takes a photo using the camer avaliable in the device
"""

from datetime import datetime
import os
import cv2


def capture():
    """
    capture a photo and save it with the title as the current time
    """
    path = os.getcwd()
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        cv2.imshow("image", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        title = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    cv2.imwrite(f"{path}/Images/images/{title}.jpg", frame)
    cv2.destroyWindow("cam-test")
    return True


if __name__ == "__main__":
    capture()
