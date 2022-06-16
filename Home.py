from turtle import right
import cv2
import face_recognition
from PIL import Image, ImageDraw
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import numpy as np


st.set_page_config(page_title="Marvel Heroes Face Recognition", page_icon=":sparkles:" , layout="wide")


          
  
        
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()    


#Load assets
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_kh4qi0dn.json")




#Header section
with st.container():
      st.subheader("Hello, I am Ghazaleh :wave:")
      st.title("Welcome to Marvel Heroes Face Recognition")
      st.write("I am passionate about image annotation!")


#About the app
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.header("What is Marvel Heroes Face Recognition App?")
        st.write("##")
        st.write(
            """
            :zap: Marvel Heroes Face Recognition App is a face recognition application build with Python.

             

            :zap: Users can upload their images and the app will let them know the celeberity name if it is from the existing dataset or if it is unknown also it will detect faces and create bounding boxes around them!
             
            """)

        with np.right_shift:
                st_lottie(lottie_coding, height=300, key="coding")




#About the different pages.
with st.container():     
    st.write("---")
    st.write("##")
    st.write("##")
    st.write(
            """
            We have 5 different pages in this website:

           :speech_balloon: Home: The first page that will be open for users. (you are seeing it now!)

           :speech_balloon: Dataset: The second page where users can see all the dataset for the application.

           :speech_balloon: Application: The third page where users can find the Marvel Heroes Face Recognition App.

           :speech_balloon: Training: The fourth page where users can find useful videos regarding Image Annotation.

           :speech_balloon: The last page where users can comunicate and send me emails!
            """)

    st.write("##")
    st.write(
            """
            You can find these 5 pages at the left side of the window.
            """)



        







