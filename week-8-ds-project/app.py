# from flask import Flask, request, render_template
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import io

# app = Flask(__name__)

# model = load_model('animal_detection_model.h5')
# model.make_predict_function()

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         img = request.files['image']
#         img = io.BytesIO(img.read())
#         img = image.load_img(img, target_size=(224, 224))
#         img = image.img_to_array(img)
#         img = np.expand_dims(img, axis=0)
#         img = img/255

#         prediction = model.predict(img)
#         predicted_class = np.argmax(prediction[0])
#         class_names = ['Bear', 'Brown Bear', 'Bull', 'Butterfly', 'Camel', 'Canary', 'Cat', 'Cattle', 'Centipede', 'Cheetah', 'Chicken', 'Crab', 'Crocodile', 'Dog', 'Duck', 'Leopard', 'Lion', 'Polar Bear', 'Tiger', 'Zebra'] # update this with your class names
#         predicted_class_name = class_names[predicted_class]

#         return render_template('index.html', prediction=predicted_class_name)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()




# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model
# model = load_model('./animal_detection_model.h5')

# # Define a list of class labels (replace with your own class labels)
# class_labels = ['class1', 'class2', 'class3', 'class4']

# # Define a function to preprocess the image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = x / 255.0  # normalize pixel values to [0, 1]
#     return x

# # Define a function to predict the class label
# def predict_class(img_path):
#     x = preprocess_image(img_path)
#     preds = model.predict(x)
#     predicted_class_idx = np.argmax(preds[0])
#     predicted_class = class_labels[predicted_class_idx]
#     return predicted_class

# # Define the route for the home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Define the route for image upload
# @app.route('/upload', methods=['POST'])
# def upload():
#     # Get the uploaded file from the request
#     file = request.files['image']

#     # Save the uploaded file to a temporary location
#     file_path = 'tmp/' + file.filename
#     file.save(file_path)

#     # Call the predict_class function to get the predicted class label
#     predicted_class = predict_class(file_path)

#     # Return the predicted class label to the user
#     return f'Predicted Class: {predicted_class}'

# if __name__ == '__main__':
#     app.run(debug=True)



import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

from flask import Flask , request, render_template
# secure_filename will ensure the images uploaded will get saved in the uploads folder
# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = load_model("./animal_detection_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        # This extracts the filepath of the image uploaded
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        # This appends the original filepath to that of uploads
        filepath = os.path.join(basepath,'tmp',f.filename)
        print("upload folder is ", filepath)
        # This saves the filepath of the image
        f.save(filepath)
        
        file = "/tmp/" + f.filename
        
        # Testing the model
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        preds = model.predict(x)
        
        print("prediction",preds)
            
        index = ['bear','crow','elephant','racoon','rat']
        
        print(np.argmax(preds))
        
        result = "The predicted animal is: " + str(index[np.argmax(preds)])
        
        return render_template("index.html", result=result, uploaded_image=file)

if __name__ == '__main__':
    app.run(debug = True, threaded = False)
