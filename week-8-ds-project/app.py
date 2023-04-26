import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

# Define the upload folder and allowed file types
UPLOAD_FOLDER = './tmp'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Load the trained model
model = load_model('animal_detection_model.h5')

# Define a dictionary that maps class indices to class names
class_dict = {
    0: 'Bear',
    1: 'Brown bear',
    2: 'Bull',
    3: 'Butterfly',
    4: 'Camel',
    5: 'Canary',
    6: 'Caterpillar',
    7: 'Cattle',
    8: 'Centipede',
    9: 'Cheetah',
    10: 'Chicken',
    11: 'Crab',
    12: 'Crocodile',
    13: 'Deer',
    14: 'Duck',
    15: 'Eagle',
    16: 'Elephant',
    17: 'Fish',
    18: 'Fox',
    19: 'Frog',
    20: 'Giraffe',
    21: 'Goat',
    22: 'Goldfish',
    23: 'Goose',
    24: 'Hamster',
    25: 'Harbor seal',
    26: 'Hedgehog',
    27: 'Hippopotamus',
    28: 'Horse',
    29: 'Jaguar',
    30: 'Jellyfish',
    31: 'Kangaroo',
    32: 'Koala',
    33: 'Ladybug',
    34: 'Leopard',
    35: 'Lion',
    36: 'Lizard',
    37: 'Lynx',
    38: 'Magpie',
    39: 'Monkey',
    40: 'Moths and butterflies',
    41: 'Mouse',
    42: 'Mule',
    43: 'Ostrich',
    44: 'Otter',
    45: 'Owl',
    46: 'Panda',
    47: 'Parrot',
    48: 'Penguin',
    49: 'Pig',
    50: 'Polar bear',
    51: 'Rabbit',
    52: 'Raccoon',
    53: 'Raven',
    54: 'Red panda',
    55: 'Rhinoceros',
    56: 'Scorpion',
    57: 'Sea lion',
    58: 'Sea turtle',
    59: 'Seahorse',
    60: 'Shark',
    61: 'Sheep',
    62: 'Shrimp',
    63: 'Snail',
    64: 'Snake',
    65: 'Sparrow',
    66: 'Spider',
    67: 'Squid',
    68: 'Squirrel',
    69: 'Starfish',
    70: 'Swan',
    71: 'Tick',
    72: 'Tiger',
    73: 'Tortoise',
    74: 'Turkey',
    75: 'Turtle',
    76: 'Whale',
    77: 'Woodpecker',
    78: 'Worm',
    79: 'Zebra'
}


# Define a function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    
    # Check if the file has an allowed extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'})
    
    # Save the file to the upload folder
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    
    # Load the image and preprocess it
    img = load_img(os.path.join(UPLOAD_FOLDER, filename), target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.
    
    # Make a prediction using the model
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    
    # Look up the predicted class name in the class dictionary
    predicted_class_name = class_dict[predicted_class_index]
    
    # # Return the predicted class name
    # return jsonify({'class': predicted_class_name})

    # Return the predicted class name and the image file path
    return render_template('index.html', predicted_class_name=predicted_class_name, image_file_path=f'/uploads/{filename}')

# Add a new route to serve the uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
