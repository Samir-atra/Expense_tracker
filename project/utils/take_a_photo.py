import cv2 as cv

def capture():

    cam = cv.VideoCapture(0)   
    s, img = cam.read()
    if s:
        # ret, frame = cam.read()
        cv.imshow('image', img)
        cv.waitKey(0)
        # x = input("what is x")
        cv.imwrite("img.jpg",img)
        # cv.destroyWindow("cam-test")
    return True

if __name__ == "__main__":
    capture()