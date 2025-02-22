import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'best_saved_model.keras'
model = load_model("best_saved_model.keras")

print(model)

print("Model Loaded Successfully")

def predict(img):
    img_resize = cv2.resize(img, (128, 128))
    rgb_img = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
    img_rank4 = np.expand_dims(rgb_img / 255, axis=0)  # Normalize and expand dimensions
    predictions = model.predict(img_rank4)
    predicted_class = np.argmax(predictions, axis=1)[0]  
    lab = ['Tomato - Healthy', 'Tomato_disease']
    print(predicted_class)
    return lab[predicted_class]


if __name__ == "__main__":
    plant = cv2.imread(r'Data\test\Tomato__d2.JPG')
    predict(plant)

