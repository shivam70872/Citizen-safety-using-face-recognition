import cv2
video = cv2.VideoCapture(0)
while True:
    flag, img = video.read()

    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    face = cascade.detectMultiScale(img, 1.1, 4)
    # print(face)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('My Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
