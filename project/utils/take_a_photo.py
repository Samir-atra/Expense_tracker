import cv2 as cv

def capture():

    cam = cv.VideoCapture(0)   
    # s, img = cam.read()
    while (True):
        ret, frame = cam.read()
        cv.imshow('image', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        # x = input("what is x")
        cv.imwrite("img.jpg",frame)
        cv.destroyWindow("cam-test")
    return True

if __name__ == "__main__":
    capture()