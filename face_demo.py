import cv2
img = cv2.imread('admin/ak.jpg')
cascade = cv2.CascadeClassifier('admin/haarcascade_frontalface_default.xml')
face = cascade.detectMultiScale(img, 1.1, 4)
print(face)
for x,y,w,h in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (225, 225, 225), 3)
cv2.imshow('My image', img)
cv2.waitKey(0)