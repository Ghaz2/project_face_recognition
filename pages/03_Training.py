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



#Removing Made with Streamlit, Hamburger Icon Menu & Streamlit Header
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}

                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)      




#Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  


#Load assets
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_xh83pj1c.json")



#Header section
with st.container():
      
      st.title("Training  :mortar_board:")
     


#About the Training
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.header("Are you passionate about image annotation?")
        st.write("##")
        st.write(
        """
        If your answer is yes, Training section is the best option for you! :heart:

        I have recorded some training regarding Image Annotation which you can watch them here.

        """)

    with np.right_shift:
                st_lottie(lottie_coding, height=300, key="coding")


#Day 1

#video 1
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.header("Day 1")
        st.write("##")
        st.subheader(":thought_balloon: Video 1")
        st.write(
            """
            In this video we will learn:

           :ballot_box_with_check: The definition of image annotation.

           :ballot_box_with_check:  Different types of annotation.

           :ballot_box_with_check: The use of annotation.

             
            """)

video1 = open("1.mp4" , "rb")
st.video(video1)

st.write("##")
#video 2
with st.container():     
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.subheader(":thought_balloon: Video 2")
        st.write(
            """
            In this video we will learn:

            :ballot_box_with_check: The introduction to Image Collection
            
            """)


vidoe2 = open("2.mp4" , "rb")
st.video(vidoe2)
      


st.write("##")
#video 3
with st.container():     
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.subheader(" :thought_balloon:Video 3")
        st.write(
            """
            In this video we will learn:

            :ballot_box_with_check: How to collect images!
            
            """)


vidoe3 = open("day1_part3.mp4" , "rb")
st.video(vidoe3)



st.write("##")
#Day 2
#Video 1
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.header("Day 2")
        st.write("##")
        st.subheader(":thought_balloon: Vidoe 1")
        st.write(
            """
            In this video we will learn:

           :ballot_box_with_check: The defenition of image annotation with Tagging method
            
            """)
vidoe1 = open("3.mp4" , "rb")
st.video(vidoe1)
 

st.write("##")
#Video 2
with st.container():     
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.subheader(" :thought_balloon:Vidoe 2")
        st.write(
            """
            In this video we will learn:

            :ballot_box_with_check: what Supervisely is!
            
            """)
vidoe2 = open("day2video2.mp4" , "rb")
st.video(vidoe2)

st.write("##")
#Video 3
with st.container():     
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.subheader(":thought_balloon: Vidoe 3")
        st.write(
            """
            In this video we will learn:

           :ballot_box_with_check: How to open Supervisely!
            
            """)
vidoe3 = open("day2video3.mp4" , "rb")
st.video(vidoe3)




st.write("##")
#Day 3
#Video 1
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.header("Day 3")
        st.write("##")
        st.subheader(":thought_balloon: Video 1")
        st.write(
            """
            In this video we will learn:

           :ballot_box_with_check: The defenition of image annotation with bounding box method
            
            """)
vidoe1 = open("4.mp4" , "rb")
st.video(vidoe1)

st.write("##")
#Video 2
with st.container():     
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.subheader(":thought_balloon: Vidoe 2")
        st.write(
            """
            In this video we will learn:

            :ballot_box_with_check: How to annotate images with bounding box method.
            
            """)
vidoe2 = open("Day3video2.mp4" , "rb")
st.video(vidoe2)


