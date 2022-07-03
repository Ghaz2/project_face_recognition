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


img =Image.open("Hero, Iron man, minimalist, 1080x2160 wallpaper.jpg")
st.sidebar.image(img)

        
#Removing Made with Streamlit, Hamburger Icon Menu & Streamlit Header
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}

                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
        
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()    


#Load assets
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_av0ub7mb.json")



#Header section
with st.container():
     
      st.title(":bomb: Welcome to Marvel Heroes Face Recognition")
      st.write("##")
      st.write("I am passionate about image annotation!")
      st.write("##")
      st.write("##")
      st.write("##")


#About the app
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.header("What is Marvel Heroes Face Recognition App?")
        st.write("##")
        st.write("##")
        st.write(
            """
           :link: Marvel Heroes Face Recognition App is a face recognition application build with Python.

             

            :link: Users can upload their images and the app will let them know the celebrity  name if it is from the existing dataset or if it is unknown also it will detect faces and create bounding boxes around them!
             
            """)

        with np.right_shift:
                st_lottie(lottie_coding, height=300, key="coding")






#About the different pages.
with st.container():     
    st.write("---")
    st.write("##")
    st.write("##")
    st.header("We have 5 different pages in this website:")
    st.write("##")
    st.write(
            """
           :black_circle: Home: The first page that will be open for users. (you are seeing it now!)
           :black_circle: Dataset: The second page where users can see all the dataset for the application.
           :black_circle: Application: The third page where users can find the Marvel Heroes Face Recognition App.
           :black_circle: Training: The fourth page where users can find useful videos regarding Image Annotation.
           :black_circle: Contact: The last page where users can communicate and send me emails!
            """)
    st.write("##")
    st.write(
            """
            You can find these 5 pages at the left side of the window.
            """)



        







