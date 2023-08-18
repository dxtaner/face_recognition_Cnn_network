import cv2
import os
import numpy as np
from PIL import Image
import time

paths=[]
names=[]

for users in os.listdir("../yuzverilerim"):
    names.append(users)
    #print(users)
#print(len(names))
#print(names)

for name in names:

    for resim in os.listdir("yuzverilerim/{}".format(name)):

        path_string = os.path.join("yuzverilerim\{}".format(name), resim)

        #yuzverilerim/taner/1_1.jpg
        #  print(resim)
        #print(path_string)
        #print(paths)
        paths.append(path_string)

#print(paths)
#print(len(paths))

faces = []
ids = []

for image_path in paths:

    image = Image.open(image_path).convert("L")
    image_Np = np.array(image,"uint8")

    faces.append(image_Np)

    #id = image_path.split(("\\"))
    #id = image_path.split(("\\"))[2]
    #id = image_path.split(("\\"))[2].split("_")

    id = int( image_path.split("\\")[2].split("_")[0] )
    ids.append(id)
    #print(id)

print("Yuz Verileri Eğitiliyor..")

time.sleep(2)
ids = np.array(ids)
print(ids)
trainer = cv2.face.LBPHFaceRecognizer_create()
trainer.train(faces, ids)
trainer.write("training/training.yml")
print("Eğitme işlemi tamamlandi...")