
Face Recognition Application with OpenCV and Python
===================================================

Getting Started
---------------

These steps outline the prerequisites and steps required to run the project on a local machine.

### Prerequisites

*   Python 3
*   OpenCV library
*   NumPy library
*   PIL (Python Imaging Library)
*   SQLite3

### Installation

1.  Clone the project to a local directory:
    
        git clone https://github.com/dxtaner/face_recognition_Opencv_and_Cnn_network.git
    
2.  Navigate to the project directory:
    
        cd directory
    
3.  Generate training data to train the face recognition model:
    
        python imageFace.py
        python cameraFace.py
    
4.  Train the face recognition model:
    
        python trainData.py
    
5.  To perform face recognition using the camera, run the following command:
    
        python cameraFace.py
    
6.  To perform face recognition on an image, use the following command:
    
        python faceIdRecog.py
    

File Descriptions
-----------------

*   `faceIdRecog.py`: This file uses the trained face recognition model to recognize faces in a live video stream.
*   `faceRecog.py`: This file uses the trained face recognition model from the `model1.h5` file to recognize faces in a live video stream.
*   `cameraFace.py`: This file detects and recognizes faces in a live video stream using the camera.
*   `imageFace.py`: This file detects and recognizes faces in an image file.
*   `kisiler.py`: This file contains a class for person data and a class for database operations.
*   `kisiler.db`: This file stores the person data and database operations.
*   `trainData.py`: This file is used to generate training data and train the face recognition model.

Usage
-----

To run the face recognition application, follow these steps:

1.  Run the `cameraFace.py` file to recognize faces in a live video stream using the camera.
2.  Run the `imageFace.py` file to recognize faces in an image.

* * *

Face Recognition Project with Keras and CNN in Python
=====================================================

Description
-----------

This project demonstrates how to create and train a face recognition model. The project is developed using the Keras and TensorFlow libraries.

Requirements
------------

*   Python 3.x
*   Keras 2.4.3
*   TensorFlow 2.4.1

Installation
------------

1.  Install the required libraries by running the following command:
    
        pip install keras tensorflow
    
2.  Clone the GitHub repository of this project:
    
        git clone https://github.com/user/face-recognition-project.git
        cd face-recognition-project
    
3.  To connect your Google Drive account to the project folder, follow these steps:
    *   If you are using Google Colab, execute the `drive.mount("/content/drive")` line provided in your code.
    *   If you are working on your local environment, install the `google-drive-ocamlfuse` package by running the following commands:
        
            sudo add-apt-repository ppa:alessandro-strada/ppa
            sudo apt-get update
            sudo apt-get install google-drive-ocamlfuse
        

Data Preparation
----------------

1.  Create a `data` folder containing the training and validation data. The folder structure should be as follows:
    
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
                
    
    *   Each class should have its own subfolder named after the class.
    *   Training data should be placed in the `train` folder, and validation data should be placed in the `validation` folder.
2.  After collecting the dataset, you can use the following code to resize the images to the appropriate size:
    
        from PIL import Image
        import os
        
        def resize_images(directory, size):
            for filename in os.listdir(directory):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(directory, filename)
                    img = Image.open(image_path)
                    img = img.resize(size)
                    img.save(image_path)
        
        # Resize training data
        resize_images("data/train", (224, 224))
        
        # Resize validation data
        resize_images("data/validation", (224, 224))
    
3.  To further diversify your dataset, you can optionally use data augmentation techniques on the images. The `ImageDataGenerator` class used in the example code is used to perform data augmentation.

Training
--------

1.  Open the `face_recognition.ipynb` file in Jupyter Notebook or Google Colab.
2.  Adjust the file paths in the code cells according to your project's file structure:
    
        os.chdir("/content/drive/My Drive/face recognition/")
        train_data_gen.flow_from_directory(directory="/content/drive/My Drive/face recognition/data/train", ...)
        val_data_gen.flow_from_directory(directory="/content/drive/My Drive/face recognition/data/validation", ...)
    
3.  Execute the code cells sequentially to train the model.
4.  Once training is complete, the trained model will be saved as `model1.h5`.

Usage
-----

1.  Load the trained model:
    
        from keras.models import load_model
        
        model = load_model("model1.h5")
    
2.  Prepare the input image for face recognition and feed it to the model:
    
        # Prepare the image for face recognition
        # ...
        
        # Use the model to recognize the face
        prediction = model.predict(image)
    

License
-------

This project is licensed under the MIT license. For more information, see the `LICENSE` file.
