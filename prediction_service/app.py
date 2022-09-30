import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np



"""
## workflow

"""

model = tf.keras.models.load_model("model.h5")  ## Loading our model
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = Image.open(uploaded_file)  ## reading the image
    img = image.resize((224,224)) ## resizing the image
    img_array = np.array(img)  ## changing the datatype of image
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel] expanding the image
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]] 

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    if argmax_index[0] == 0:
        st.image(image, caption="predicted: cat")
    else:
        st.image(image, caption='predicted: dog')
      









