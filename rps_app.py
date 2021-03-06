# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:40:50 2020

@author: ASUS
"""

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps

def import_and_predict(image_data, model):
    
        size = (75,75)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)

        img_reshape = image[np.newaxis,...]

        prediction = model.predict(img_reshape)
        
        return prediction

model = tf.keras.models.load_model('cotton.hdf5')

st.write("""
         # Cotton Diseases
         """
         )

st.write("This is a simple image classification web app to predict Cotton Diseases develop by NAVDEEP MEHTA")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
#
if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("diseased cotton leaf")
    elif np.argmax(prediction) == 1:
        st.write("diseased cotton plant")
    elif np.argmax(prediction) == 2:
        st.write("fresh cotton leaf")
    else:
        st.write("fresh cotton plant")
    
    st.text("Probability (0: Diseased_Leaf, 1: Diseased_Plant, 2: Fresh_Leaf, 3: Fresh_Plant")
    st.write(prediction)