Yüz Tanıma Uygulaması OpenCv Python
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

Yüz Tanıma Projesi

Yüz Tanıma Projesi Keras Python
==================

Gereksinimler
-------------

*   Python 3.x
*   Keras 2.4.3
*   TensorFlow 2.4.1

Kurulum
-------

1.  Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
`pip install keras tensorflow`3.  Bu projenin GitHub deposunu klonlayın:
`git clone https://github.com/kullanici/yuz-tanima-projesi.git` `cd yuz-tanima-projesi`6.  Proje klasörüne Google Drive hesabınızı bağlamak için aşağıdaki adımları izleyin:
    *   Google Colab kullanıyorsanız, kodunuzda verilen `drive.mount("/content/drive")` satırını çalıştırın.
    *   Kendi yerel ortamınızda çalışıyorsanız, `google-drive-ocamlfuse` paketini yüklemek için aşağıdaki komutu çalıştırın: `sudo add-apt-repository ppa:alessandro-strada/ppa` `sudo apt-get update` `sudo apt-get install google-drive-ocamlfuse`

Veri Hazırlığı
--------------

1.  Eğitim ve doğrulama verilerini içeren `data` klasörünü oluşturun. Klasör yapısı şu şekilde olmalıdır:
    
    data/
      |- train/
      |  |- class1/
      |  |- class2/
      |  |- class3/
      |
      |- validation/
         |- class1/
         |- class2/
         |- class3/
                
    
    *   Her sınıfın kendi adını taşıyan bir alt klasörü olmalıdır.
    *   Eğitim verileri `train` klasörüne, doğrulama verileri `validation` klasörüne yerleştirilmelidir.
2.  Veri kümesini hazırlamak için, her sınıf için yeterli sayıda görüntü toplayın ve etiketleyin. Görüntüleri uygun alt klasörlere yerleştirin.

Model Eğitimi
-------------

1.  `yüz_tanıma.ipynb` dosyasını Jupyter Notebook veya Google Colab üzerinde açın.
2.  Kod hücrelerindeki dosya yollarını projenizin dosya yapısına göre düzenleyin:
`os.chdir("/content/drive/My Drive/yüz tanıma/")` `train_data_gen.flow_from_directory(directory="/content/drive/My Drive/yüz tanıma/data/train", ...)` `val_data_gen.flow_from_directory(directory="/content/drive/My Drive/yüz tanıma/data/validation", ...)`6.  Modeli eğitmek için kod hücrelerini sırasıyla çalıştırın.
7.  Eğitim tamamlandığında, eğitilmiş model `model1.h5` olarak kaydedilecektir.

Kullanım
--------

1.  Eğitilmiş modeli yükleyin:

from keras.models import load\_model

model = load\_model("model1.h5")
        

3.  Yüz tanıma işlemi için giriş görüntüsünü hazırlayın ve modele verin:

\# Görüntüyü yüz tanıma için hazırla
# ...

# Modeli kullanarak yüzü tanı
prediction = model.predict(image)
        

Lisans
------

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.


