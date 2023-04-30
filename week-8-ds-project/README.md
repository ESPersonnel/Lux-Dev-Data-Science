# Week 8: Final Capstone Project

## Animal Detection Model and Web Application

### Overview

In this project, I created a deep learning model for animal detection and deployed it as a web application using Flask. The model is trained on a dataset of animal images and can classify images into different animal categories. Users can upload images through the web application and receive predictions on the animal class.


### Dataset

The dataset used in this project is available on ![Kaggle](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset). It contains images of various animals (80 animals, excluding the infamous dogs and cats), divided into training and testing sets. The dataset is preprocessed using the ImageDataGenerator class from TensorFlow, which rescales the images, applies data augmentation techniques, and generates batches of images for training and validation.


### Model

The model is based on the DenseNet121 architecture, which is a pre-trained convolutional neural network. The DenseNet121 model is fine-tuned by adding a global average pooling layer, a dropout layer, a dense layer with 1024 units, and a final dense layer with the number of classes in the dataset. The model is trained using the Adam optimizer with a learning rate of 0.001, categorical crossentropy loss, and accuracy as the evaluation metric.

### Flask Web Application

The Flask web application allows users to upload images and receive predictions on the animal class. The application includes the following routes:

    /: Renders the main page with a file upload form.
    /upload: Handles file uploads, preprocesses the image, makes a prediction using the trained model, and returns the predicted class name.
    /uploads/<filename>: Serves the uploaded images.

The main page of the web application contains a form that allows users to upload an image. Once the image is uploaded, it is preprocessed and passed through the trained model to obtain a prediction. The predicted class name is then displayed on the page along with the uploaded image.

### Template

The index.html file is the template for the main page of the Flask web application. It includes a form for uploading images, a section for displaying the uploaded image, and a section for displaying the predicted animal class.
Usage
To run the Flask web application, execute the following command:

    python app.py

This will start the Flask development server, and the application will be accessible at http://127.0.0.1:5000/.

### File Structure

```
├── app.py
├── animal_detection_cv5.ipynb
├── animal_detection_model.h5
├── templates
│   └── index.html
└── tmp
    └── uploaded_image.jpg
```


### Conclusion

This project demonstrates how to create a deep learning model for animal detection and deploy it as a web application using Flask. The model is trained on a dataset of animal images and can classify images into different animal categories. Users can upload images through the web application and receive predictions on the animal class.


