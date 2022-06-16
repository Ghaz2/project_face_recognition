import streamlit as st


# Text

st.title("This is a title")
st.header("This is a header.")
st.subheader("This is a subheader.")
st.write("Hell World")

for i in range(3):
    st.write("I hope you like my thesis!")

# Status Banner
st.success("This is successful!")
st.warning("This is warning!")
st.error("This is error!")


# Show image
from PIL import Image
img = Image.open("group.jpg")
st.image(img, width = 300, caption = "This is a caption")


# Upload Image/File
img2 = st.file_uploader("upload an image file:", type=['jpg', 'jpeg', 'png'])
st.image(img2, width = 300, caption = "You choose this file.")


# Buttons
if st.button("This is a button"):
    st.text("You just clicked a button")

    st.balloons()