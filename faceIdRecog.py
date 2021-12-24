from kisiler import *
import cv2
import os
from math import ceil

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("training/trainer.yml")

kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#kamera.set(3, 1000)
#kamera.set(4, 800)
font = cv2.FONT_HERSHEY_SIMPLEX

#kisiler verisi
kisiler=Kisiler()

while True:
    ret, cam = kamera.read()

    gri_toncam = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gri_toncam,scaleFactor=1.3,minNeighbors=5,minSize=(100,100))

    for(x, y, w, h) in faces:
        cv2.rectangle(cam, (x, y), (x + w, y + h), (0, 255, 0), 3)
        id,oran = recognizer.predict(gri_toncam[y:y + h, x:x + w])

        if (oran<100):
            print(id)
            name = kisiler.isimverisiniCek(id)
        else:
            name = "Bilinmeyen kisi"
            oran = 100

        cv2.putText(cam, name, (x + 5, y - 5), font,1.2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(cam, str(ceil(100-oran)) + "%", (x + 5, y + h - 5), font, 1.2, (255, 255, 0), 5)

    cv2.imshow("Kamera Goruntusu", cam)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()