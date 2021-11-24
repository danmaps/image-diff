import numpy as np
import streamlit as st
from PIL import Image, ImageChops

def get_diff(im1,im2):
    diff = Image.open("image_diff.jpg")
    diff.paste(Image.open(im1).resize([590,427]), (49, 45))
    diff.paste(Image.open(im2).resize([590,427]), (679, 150))
    
    return diff

def images_are_equal(image1,image2):
    if list(Image.open(image1).getdata()) == list(Image.open(image2).getdata()):
        return True
    else:
        return False

def check_dims(image1,image2):
    buffer1 = np.asarray(Image.open(image1))
    buffer2 = np.asarray(Image.open(image2))

    if buffer1.shape==buffer2.shape:
        return True
    else:
        st.write("images are different dimensions...")
        st.image(Image.open(image1), caption=f"image1:{buffer1.shape}")
        st.image(Image.open(image2), caption=f"image2:{buffer2.shape}")
        return False

def subtract_images(image1,image2):
    buffer1 = np.asarray(Image.open(image1))
    buffer2 = np.asarray(Image.open(image2))

    return Image.fromarray(buffer1 - buffer2)


# Uploading the files to the page
uploadFile1 = st.file_uploader(label="Upload image 1", type=['jpg', 'png'])
uploadFile2 = st.file_uploader(label="Upload image 2", type=['jpg', 'png'])

if uploadFile1 is not None:
    oneimage = st.image(get_diff(uploadFile1,uploadFile1), caption='',use_column_width=True)
    if uploadFile2 is not None:
        oneimage.empty()
        if images_are_equal(uploadFile1,uploadFile2):
            # they're the same picture
            twoimage = st.image(get_diff(uploadFile1,uploadFile2), caption='',use_column_width=True)
        else:
            # they're different pictures...
            twoimage = st.image(get_diff(uploadFile1,uploadFile2), caption='',use_column_width=True)


            # if they have the same dimensions, we can subtract them to visually inspect differences
            if check_dims(uploadFile1,uploadFile2):
                st.write("here they are subtracted...")
                subtraction = subtract_images(uploadFile1,uploadFile2)
                st.image(subtraction)


# on launch show the empty template
else:
    st.image(Image.open("image_diff.jpg"), caption='',use_column_width=True)
