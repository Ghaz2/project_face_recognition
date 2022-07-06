
import cv2
import face_recognition
from PIL import Image, ImageDraw
from pandas import concat
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import numpy as np



st.set_page_config(page_title="Marvel Heroes Face Recognition", page_icon=":sparkles:" , layout="wide")



img =Image.open("Halk2.jpg")
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




#Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me! :email:")
    st.write("---")
    st.write("##")



from PIL import Image, ImageDraw
from pandas import concat
import requests
import streamlit as st

import numpy as np



st.set_page_config(page_title="Marvel Heroes Face Recognition", page_icon=":sparkles:" , layout="wide")



img =Image.open("Halk2.jpg")
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




#Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me! :email:")
    st.write("---")
    st.write("##")



contact_form = """
<form action="https://formsubmit.co/ghazalehalba@gmail.com" method="POST">
     <input type="hidden"  name="_captcha" value="false">
     <input type="text"  name="name" placeholder="Please enter your name" required>
     <input type="email"  name="name" placeholder="Please enter your email" required>
     <textarea name="message" placeholder="Please type your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""    

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()    


#Use local css
def local_css(file_name):
 with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True )
local_css("style/style.css")        


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()    


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  