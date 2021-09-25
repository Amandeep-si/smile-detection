import numpy as np
import cv2


# we use two haarcascade files which have an information of face detection and simile detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# opening the webcam to access the default webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, img = cap.read()
    # here we read the images of the camera by using cap.read() and store in a img variable and ret is a falg which specifies that our camera is properly working or not
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # we convert the image into gray color using cvtColor()
    faces = faceCascade.detectMultiScale(  # it will read the image and detect an object in image
        gray,  # Initialise the face cascade
        scaleFactor=1.3,  # size of the image
        minNeighbors=5,  # minimum number of object for detection in image
        minSize=(30, 30)  # minimum size of the face in an image
    )

    for (x, y, w, h) in faces:  # read the face detected in image and place x-y coordinates with width and height
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # draw a rectangle and with color code and its width
        roi_gray = gray[y:y + h, x:x + w]
        # we specify now our reigion of interest i.e our face stored in a gray

        smile = smileCascade.detectMultiScale(
            roi_gray,  # initialise the smile cascade
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25, 25),
        )

        for i in smile:
            if len(smile) > 1:
                cv2.putText(img, "You're Smiling", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
