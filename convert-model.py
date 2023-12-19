import tensorflow as tf
from tensorflow import keras

# Lodaing best model
model = keras.models.load_model('resnet_50_v117_0.920.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('butterfly-model.tflite', 'wb') as f_out:
    f_out.write(tflite_model)