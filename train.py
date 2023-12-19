"""
Capstone Project 2
Butterfly-Classification
Dashel Ruiz Perez 12/26/2023
"""

# Importing libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# Function to make the model
def make_model(learning_rate=0.01, size_inner1=512, size_inner2=256, size_inner3=256, input_shape=150):
    base_model = ResNet50(weights='imagenet', 
                          include_top = False,
                          input_shape=(input_shape,input_shape,3))
    base_model.trainable = False

    #################################################################################
    inputs = keras.Input(shape=(input_shape,input_shape,3))
    base = base_model(inputs, training=False)
    vectors = keras.layers.GlobalAveragePooling2D()(base)
    inner1 = keras.layers.Dense(512, activation='relu')(vectors)
    inner2 = keras.layers.Dense(256, activation='relu')(inner1)
    inner3 = keras.layers.Dense(256, activation='relu')(inner2)      
    outputs = keras.layers.Dense(75)(inner3)
    model = keras.Model(inputs, outputs)

    ##################################################################################
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    
    loss = keras.losses.CategoricalCrossentropy(from_logits=True)
    
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

    return model


# Variables
learning_rate = 0.001
input_size = 224

# Making the generator with data augmentation
train_gen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20, # rotate the image slightly between 0 and 20 degrees (note: this is an int not a float)
    shear_range=0.2, # shear the image
    zoom_range=0.2, # zoom into the image
    width_shift_range=0.2, # shift the image width ways
    height_shift_range=0.2, # shift the image height ways
    horizontal_flip=True
)


# Prepare the dataset for the neural network
path ='/home/dashel/Documents/zoomcamp/capstone-2/butterfly-image-classification/train'
val_path ='/home/dashel/Documents/zoomcamp/capstone-2/butterfly-image-classification/valid'

train_ds = train_gen.flow_from_directory(
    path,
    target_size=(input_size, input_size),
    batch_size=32
)

val_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

val_ds = train_gen.flow_from_directory(
    val_path,
    target_size=(input_size, input_size),
    batch_size=32,
    shuffle=False
)

# Callback to save the best model
checkpoint = keras.callbacks.ModelCheckpoint(
    'resnet_50_v2{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only=True,
    monitor='val_accuracy',
    mode='max'
)


# Making the model
model = make_model(
        learning_rate=learning_rate, input_shape=input_size
    )

history = model.fit(train_ds, epochs=10, validation_data=val_ds)