from kisiler import *
import cv2
import numpy as np
import cvlib as cv

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("../training/trainer.yml")

kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#kamera.set(3, 1920)
#kamera.set(4, 1080)
font = cv2.FONT_HERSHEY_SIMPLEX

# kisiler verisi
kisiler = Kisiler()


while kamera.isOpened():
    ret, cam = kamera.read()

    gri_toncam = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)  # yuz_tanıma
    yuz, confidence = cv.detect_face(cam)

    for idx, face in enumerate(yuz):
        # print(yuz)
        (startX, startY) = face[0], face[1]
        (endX, endY) = face[2], face[3]

        cv2.rectangle(cam, (startX, startY), (endX, endY), (0, 0, 255), 3)
        image_b = np.copy(gri_toncam[startY:endY, startX:endX])

        if (image_b.shape[0]) < 10 or (image_b.shape[1]) < 10:
            continue
        b = image_b

        idx, conf = recognizer.predict(b)
        print("id",idx)
        print("conf", conf)
        if (conf < 100):
            label = kisiler.isimverisiniCek(idx)
            label = "{}:{:.2f}%".format(label, 100 - conf)
        else:
            label = "bilinmeyen kisi"
            # print(idx)

        cv2.putText(cam, label, (startX + 2, startY - 5), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Kamera Goruntusu", cam)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()