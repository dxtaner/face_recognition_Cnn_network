from kisiler import *
import cv2
import os
import time

kamera=cv2.VideoCapture(0)
yuzdedektor=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

adet=0

try:

    name = input("İsim girin:")

    yuzid = input("Yüz id'sini giriniz:")

    kisiler = Kisiler()
    newKisi = Kisi(int(yuzid), name)

    print("Veritabanina Kisi Ekleniyor")
    time.sleep(2)
    kisiler.kisiekle(newKisi)
    print("Veritabanina Kişi Eklendi")

    yol = 'yuzverilerim/' + name + '/'
    os.mkdir(yol)

    print("Kameraya bakın ve bekleyin...")

    while True:
        ret, goruntu = kamera.read()
        griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
        yuzler = yuzdedektor.detectMultiScale(griton, scaleFactor=1.4, minNeighbors=5,
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in yuzler:
            cv2.rectangle(goruntu, (x, y), (x + w, y + h), (255, 255, 255), 6)

            adet += 1
            cv2.imwrite(yol + yuzid + "_" + str(adet) + ".jpg", griton[y:y + h, x:x + w])
            # "yuzverilerim/Taner/1_1.jpg"

            cv2.imshow("kameradan yuz tarama", goruntu)

        if (cv2.waitKey(30) & 0xFF == ord('q')):
            break

        elif adet > 99:
            break

    print("Yüz verileri kaydedildi.\nProgram Sonlanıyor...!")

    kamera.release()
    cv2.destroyAllWindows()

except ValueError:
    print("Lüfen Veri Değerlerini Kendi Formatında Giriniz..!!")
except OSError as exc:
    print("Dizin Yolu Hatası {} dizin yolu önce tanımlanmıs farklı isim girin ".format(name))
except sqlite3.IntegrityError:
    print("Primary Key Hatası\nDaha önce {} yuzidsi Eklenmis!! Lütfen Farklı Girin ".format(yuzid))





