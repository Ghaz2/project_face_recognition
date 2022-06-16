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


#Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  


#Load assets
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_QYKV0O.json")

#Header section
with st.container():
      st.title("Application :bomb:")
      

#About the dataset
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.write(
            """
            Here users can find the Marvel Heroes Face Recognition Application!
            
            
            Each user can upload an image and our app will recognize the Marvel Hero or will show Unkown tag, also our app will detect the face and will draw a bounding box around it!



            
            
            """)


        with np.right_shift:
                st_lottie(lottie_coding, height=300, key="coding")



# known images

known_face_encodings = []    # list of encodings
known_face_names = []        # list of person's name
known_face_faces = []        # list of person's photo
    
def train_encodings(img, img_name):
    image_of_person = face_recognition.load_image_file(img)
    encoding_of_person = face_recognition.face_encodings(image_of_person)[0]

    known_face_encodings.append(encoding_of_person)
    known_face_names.append(img_name)
    known_face_faces.append(img)



# ADD HERE FOR FACES

Alfred_Molina= "images/Alfred_Molina.jpg"
Andrew_Garfield= "images/Andrew_Garfield.jpg"
Angelina_Jolie  = "images/Angelina_Jolie.jpg"
Anthony_Dwane_Mackie  = "images/Anthony_Dwane_Mackie.jpg"
Barry_Keoghan  = "images/Barry_Keoghan.jpg"
Benedict_Cumberbatch  = "images/Benedict_Cumberbatch.jpg"
Benedict_Wong  = "images/Benedict_Wong.jpg"
Brie_Larson= "images/Brie_Larson.jpg"
Chadwick_Boseman = "images/Chadwick_Boseman.jpg"
Chris_Pratt = "images/Chris_Pratt.jpg"
Christopher_Hemsworth = "images/Christopher_Hemsworth.jpg"
Christopher_Robert_Evans= "images/Christopher_Robert_Evans.jpg"
Donald_Frank_Cheadle = "images/Donald_Frank_Cheadle.jpg"
Elizabeth_Olsen  = "images/Elizabeth_Olsen.jpg"
Gemma_Chan = "images/Gemma_Chan.jpg"
Hayley_Elizabeth_Atwell  = "images/Hayley_Elizabeth_Atwell.jpg"
Jake_Gyllenhaal  = "images/Jake_Gyllenhaal.jpg"
Jamie_Foxx  = "images/Jamie_Foxx.jpg"
Jeremy_Renner = "images/Jeremy_Renner.jpg"
Karen_Gillan  = "images/Karen_Gillan.jpg"
Krysten_Ritter  = "images/Krysten_Ritter.jpg"
Kumail_Nanjiani = "images/Kumail_Nanjiani.jpg"
Lauren_Ridloff = "images/Lauren_Ridloff.jpg"
Letitia_Michelle_Wright = "images/Letitia_Michelle_Wright.jpg"
Mark_Ruffalo = "images/Mark_Ruffalo.jpg"
Paul_Bettany  = "images/Paul_Bettany.jpg"
Paul_Rudd = "images/Paul_Rudd.jpg"
Richard_Madden = "images/Richard_Madden.jpg"
Robert_DowneyJr = "images/Robert_DowneyJr.jpg"
Salma_Hayek = "images/Salma_Hayek.jpg"
Samuel_LJackson  = "images/Samuel_L.Jackson.jpg"
Scarlett_ngrid_Johansson = "images/Scarlett_ngrid_Johansson.jpg"
Sebastian_Stan  = "images/Sebastian_Stan.jpg"
Tessa_Thompson  = "images/Tessa_Thompson.jpg"
Thomas_William_Hiddleston = "images/Thomas_William_Hiddleston.jpg"
Tobey_Maguire  = "images/Tobey_Maguire.jpg"
Tom_Hardy = "images/Tom_Hardy.jpg"
Tom_Holland  = "images/Tom_Holland.jpg"
Willem_Dafoe  = "images/Willem_Dafoe.jpg"
Zoe_Saldana = "images/Zoe_Saldana.jpg"
Kim  = "images/Kim So-yeon.jpg"



train_encodings(Alfred_Molina,"Alfred_Molina")
train_encodings(Andrew_Garfield,"Andrew_Garfield")
train_encodings(Angelina_Jolie,"Angelina_Jolie")
train_encodings(Anthony_Dwane_Mackie,"Anthony_Dwane_Mackie")
train_encodings(Barry_Keoghan,"Barry_Keoghan")
train_encodings(Benedict_Cumberbatch,"Benedict_Cumberbatch")
train_encodings(Benedict_Wong,"Benedict_Wong")
train_encodings(Brie_Larson,"Brie_Larson")
train_encodings(Chadwick_Boseman,"Chadwick_Boseman")
train_encodings(Chris_Pratt,"Chris_Pratt")
train_encodings(Christopher_Hemsworth,"Christopher_Hemsworth")
train_encodings(Christopher_Robert_Evans,"Christopher_Robert_Evans")
train_encodings(Donald_Frank_Cheadle ,"Donald_Frank_Cheadle ")
train_encodings(Elizabeth_Olsen,"Elizabeth_Olsen")
train_encodings(Gemma_Chan,"Gemma_Chan")
train_encodings(Hayley_Elizabeth_Atwell,"Hayley_Elizabeth_Atwell")
train_encodings(Jake_Gyllenhaal,"Jake_Gyllenhaal")
train_encodings(Jamie_Foxx,"Jamie_Foxx")
train_encodings(Jeremy_Renner,"Jeremy_Renner")
train_encodings(Karen_Gillan,"Karen_Gillan")
train_encodings(Krysten_Ritter,"Krysten_Ritter")
train_encodings(Kumail_Nanjiani,"Kumail_Nanjiani")
train_encodings(Lauren_Ridloff,"Lauren_Ridloff")
train_encodings(Letitia_Michelle_Wright,"Letitia_Michelle_Wright")
train_encodings(Mark_Ruffalo,"Mark_Ruffalo")
train_encodings(Paul_Bettany,"Paul_Bettany")
train_encodings(Paul_Rudd,"Paul_Rudd")
train_encodings(Richard_Madden,"Richard_Madden")
train_encodings(Robert_DowneyJr,"Robert_DowneyJr")
train_encodings(Salma_Hayek,"Salma_Hayek")
train_encodings(Samuel_LJackson,"Samuel_L.Jackson")
train_encodings(Scarlett_ngrid_Johansson,"Scarlett_ngrid_Johansson")
train_encodings(Sebastian_Stan,"Sebastian_Stan")
train_encodings(Tessa_Thompson,"Tessa_Thompson")
train_encodings(Thomas_William_Hiddleston,"Thomas_William_Hiddleston")
train_encodings(Tobey_Maguire,"Tobey_Maguire")
train_encodings(Tom_Hardy,"Tom_Hardy")
train_encodings(Tom_Holland,"Tom_Holland")
train_encodings(Willem_Dafoe,"Willem_Dafoe")
train_encodings(Zoe_Saldana,"Zoe_Saldana")






st.write("For testing faces:")
imageTest = st.file_uploader("Please upload an image:", type=["jpg","jpeg","png"])

if imageTest is not None:
    st.write("This is the selected photo.")
    test_image = face_recognition.load_image_file(imageTest)
    st.image(test_image, width = 300)

else:
    st.warning("Please select an image!")


try:
     all_names = []

     if imageTest is not None:
         if st.button("Proceed to Test"):
             test_face_locations = face_recognition.face_locations(test_image)
             test_face_encodings = face_recognition.face_encodings(test_image, test_face_locations)

             # Display the output
             img_PIL = Image.fromarray(test_image)

             # To draw the bounding boxes
             draw = ImageDraw.Draw(img_PIL)

             # Loop through all the faces in test image
             for (topY,rightX,bottomY,leftX), test_face_encoding in zip(test_face_locations, test_face_encodings):
                 matches = face_recognition.compare_faces(known_face_encodings, test_face_encoding)
    
                 name = "Unknown"
    
                 # If match
                 if True in matches:
                    index = matches.index(True)
                    name = known_face_names[index]
                    confidence_level = face_recognition.face_distance(known_face_encodings,test_face_encoding)
                    st.write("\nName:", name)
                    st.write("Confidence:", round(np.amax(confidence_level),2))
            
                 else:
                   confidence_level = face_recognition.face_distance(known_face_encodings,test_face_encoding)
                   st.write("\nName:", name)
                   st.write("Confidence:", round(np.amax(confidence_level),2))

        
                 # draw box
                 draw.rectangle(
                     ((leftX,topY),(rightX,bottomY)),
                     outline = (255,255,0) , width = 3)
                 draw.text((leftX,topY - 20) , str(name)+"  " + str(round(np.amax(confidence_level),2)),fill = (255,255,0,255))
                 del draw
    
            # display Image
             st.image(img_PIL)


           

except:
    pass