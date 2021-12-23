import cv2
import os

res = cv2.imread("resimler/soso.jpg")
yuzcascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

adet = 0

id = input("id girin:")
name = input("isim giriniz")
yol = 'yuzverilerim/'+ name + '/'


while True:
    griton = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    yuzler = yuzcascade.detectMultiScale(griton, scaleFactor=1.3, minNeighbors=5, minSize=(100,100))

    for(x, y, w, h) in yuzler:
        yuz = cv2.rectangle(res, (x , y), (x + w, y + h), (0, 255, 0), 3)
        adet += 1
        cv2.imwrite(yol + str(id) + "_" + str(adet) + ".jpg",
                griton[y:y + h, x:x + w])
        cv2.imshow("yuzler", res)

    if (cv2.waitKey(30) & 0xFF == ord('q')):
        break
    elif adet>99:
        break


print("Yüz verileri kaydedildi.\nProgram Sonlanıyor...!")

cv2.waitKey(0)
cv2.destroyAllWindows()