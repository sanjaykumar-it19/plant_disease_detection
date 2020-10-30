'''from keras.preprocessing import image
from keras.models import load_model
import numpy as np
model = load_model('model2.h5')
print("Model Loaded Successfully")

def classify(img_file):
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (256, 256),grayscale=True)

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    arr = np.array(result[0])
    print(arr)
    maxx = np.amax(arr)
    max_prob = arr.argmax(axis=0)
    max_prob = max_prob + 1
    classes=["Background", "Diseased_leaf", "Healthy_leaf"]
    result = classes[max_prob -1 ]
    print(img_name,result)


import os
path = 'C:/Users/SANJAY KUMAR S/OneDrive/Documents/programs/Leaf disease/Dataset/Test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if '.jpg' in file:
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')'''
from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image

json_file = open('model2.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model2.h5")
print("Loaded model from disk")

def classify(img_file):
    '''img_name = img_file
    test_image = image.load_img(img_name, target_size = (128, 128))
    
    test_image = image.img_to_array(test_image)
    print('test image')
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'Healthy leaf'
    else:
        prediction = 'Diseased leaf'
    print(prediction,img_name)'''
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (128, 128))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    arr = np.array(result[0])
    print(arr)
    maxx = np.amax(arr)
    max_prob = arr.argmax(axis=0)
    max_prob = max_prob + 1
    classes=["Background", "Diseased_leaf", "Healthy_leaf"]
    result = classes[max_prob -1 ]
    print(img_name,result)



import os
path = 'C:/Users/SANJAY KUMAR S/OneDrive/Documents/programs/Leaf disease/Dataset/Test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if '.jpg' in file:
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')