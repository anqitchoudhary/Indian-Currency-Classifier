import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image, ImageOps
import numpy as np


def currency_classification(img):
   
    #MOBILENET


    model = tf.keras.models.load_model('model_Classifier.h5')

  
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
   
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

   
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) -1

   
    data[0] = normalized_image_array

    
    prediction = model.predict(data)
    score = tf.nn.softmax(prediction[0])

    return np.argmax(prediction), np.max(score)
