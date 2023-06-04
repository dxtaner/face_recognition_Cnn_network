Yüz Tanıma Uygulaması
=====================

Başlangıç
---------

Bu adımlar, projeyi yerel bir makinede çalıştırmak için gereken önkoşulları ve adımları açıklar.

### Önkoşullar

*   Python 3
*   OpenCV kütüphanesi
*   NumPy kütüphanesi
*   PIL (Python Imaging Library)
*   SQLite3

### Kurulum

1.  Projeyi yerel bir dizine klonlayın:

    git clone [https://github.com/kullanici/yuz-tanimlama-uygulamasi.git](https://github.com/dxtaner/face_recognition_Opencv_and_Cnn_network/tree/main)

3.  Proje dizinine gidin:

    cd yuz-tanimlama-uygulamasi

5.  Yüz tanıma modelini eğitmek için eğitim verilerini oluşturun:

     python imageFace.py  
     python cameraFace.py

7.  Yüz tanıma modelini eğitin:

    python trainData.py

9.  Kamera üzerinde yüz tanıma yapmak için aşağıdaki komutu çalıştırın:

    python cameraFace.py

11.  Bir görüntü üzerinde yüz tanıma yapmak için aşağıdaki komutu kullanın:
      
      python faceIdRecog.py
  

Dosyaların Açıklamaları
-----------------------

*   `faceIdRecog.py`: Bu dosya, eğitilmiş yüz tanıma modelini kullanarak canlı video akışında yüzleri tanımayı sağlar.
*   `cameraFace.py`: Bu dosya, kamerayı kullanarak canlı video akışında yüzleri algılar ve tanır.
*   `imageFace.py`: Bu dosya, bir görüntü dosyası üzerinde yüzleri algılar ve tanır.
*   `kisiler.py`: Bu dosya, kişi verilerini içeren bir sınıf ve veritabanı işlemlerini gerçekleştiren bir sınıf içerir.
*   `trainData.py`: Bu dosya, eğitim verilerini oluşturmak ve yüz tanıma modelini eğitmek için kullanılır.

Kullanım
--------

Yüz tanıma uygulamasını çalıştırmak için aşağıdaki adımları izleyin:

1.  Kamerayı kullanarak canlı video akışında yüz tanımak için `cameraFace.py` dosyasını çalıştırın.
2.  Bir görüntü üzerinde yüz tanımak için `imageFace.py` dosyasını çalıştırın.

Katkıda Bulunma
---------------

Katkıda bulunmak isterseniz, lütfen bir istek oluşturun veya bize ulaşın.

Lisans
------

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasını inceleyebilirsiniz.
