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



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  


#Load assets
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_n5icqxkw.json")


#Header section
with st.container():
      st.title("Dataset :bomb:")
      


#About the dataset
with st.container():     
    st.write("---")
    np.left_shift, np.right_shift = st.columns(2)
    with np.left_shift:
        st.write("##")
        st.write(
            """
            In Marvel Heroes Face Recognition Application we have 40 dataset.
            
            Users can find the dataset bellow.



            Each dataset contains:

            :checkered_flag:  Name
          
            :checkered_flag:  Image
    
            :checkered_flag:  Short description
            
            """)


        with np.right_shift:
                st_lottie(lottie_coding, height=300, key="coding")





#Cast of Marvel Heroes
Robert_DowneyJr = Image.open("images/Robert_DowneyJr.jpg")

Paul_Bettany = Image.open("images/Paul_Bettany.jpg")

Scarlett_ngrid_Johansson = Image.open("images/Scarlett_ngrid_Johansson.jpg")

Donald_Frank_Cheadle= Image.open("images/Donald_Frank_Cheadle.jpg")

Christopher_Robert_Evans = Image.open("images/Christopher_Robert_Evans.jpg")

Christopher_Hemsworth = Image.open("images/Christopher_Hemsworth.jpg")

Thomas_William_Hiddleston = Image.open("images/Thomas_William_Hiddleston.jpg")

Mark_Ruffalo = Image.open("images/Mark_Ruffalo.jpg")

Sebastian_Stan = Image.open("images/Sebastian_Stan.jpg")

Jeremy_Renner = Image.open("images/Jeremy_Renner.jpg")

Elizabeth_Olsen = Image.open("images/Elizabeth_Olsen.jpg")

Samuel_LJackson = Image.open("images/Samuel_L.Jackson.jpg")

Tessa_Thompson = Image.open("images/Tessa_Thompson.jpg")

Letitia_Michelle_Wright = Image.open("images/Letitia_Michelle_Wright.jpg")

Anthony_Dwane_Mackie = Image.open("images/Anthony_Dwane_Mackie.jpg")

Karen_Gillan = Image.open("images/Karen_Gillan.jpg")

Krysten_Ritter = Image.open("images/Krysten_Ritter.jpg")

Zoe_Saldana = Image.open("images/Zoe_Saldana.jpg")

Benedict_Cumberbatch = Image.open("images/Benedict_Cumberbatch.jpg")

Benedict_Wong = Image.open("images/Benedict_Wong.jpg")

Chris_Pratt = Image.open("images/Chris_Pratt.jpg")

Paul_Rudd = Image.open("images/Paul_Rudd.jpg")

Tom_Holland = Image.open("images/Tom_Holland.jpg")

Brie_LarsonC = Image.open("images/Brie_Larson.jpg")

Angelina_Jolie = Image.open("images/Angelina_Jolie.jpg")

Gemma_Chan = Image.open("images/Gemma_Chan.jpg")

Barry_Keoghan = Image.open("images/Barry_Keoghan.jpg")

Richard_Madden = Image.open("images/Richard_Madden.jpg")

Salma_Hayek = Image.open("images/Salma_Hayek.jpg")

Kumail_Nanjiani = Image.open("images/Kumail_Nanjiani.jpg")

Tom_Hardy= Image.open("images/Tom_Hardy.jpg")

Alfred_Molina = Image.open("images/Alfred_Molina.jpg")

Jamie_Foxx = Image.open("images/Jamie_Foxx.jpg")

Jake_Gyllenhaal = Image.open("images/Jake_Gyllenhaal.jpg")

Willem_Dafoe = Image.open("images/Willem_Dafoe.jpg")

Tobey_Maguire = Image.open("images/Tobey_Maguire.jpg")

Andrew_Garfield = Image.open("images/Andrew_Garfield.jpg")

Lauren_Ridloff = Image.open("images/Lauren_Ridloff.jpg")

Chadwick_Boseman = Image.open("images/Chadwick_Boseman.jpg")

Hayley_Elizabeth_Atwell = Image.open("images/Hayley_Elizabeth_Atwell.jpg")



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Christopher_Robert_Evans)
        #yes
    with text_column:
         st.header("Christopher_Robert_Evans")
         st.write(
"""
Christopher Robert Evans is an American actor, film producer, and director. Evans began his acting career in typical fashion: performing in school productions and community theatre.

He was born in Boston, Massachusetts, the son of Lisa (Capuano), who worked at the Concord Youth Theatre, and G. Robert Evans III, a dentist. His uncle is former U.S. Representative Mike Capuano. 


"""
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Scarlett_ngrid_Johansson)
        #yes
    with text_column:
         st.header("Scarlett_ngrid_Johansson")
         st.write(
"""
Scarlett Ingrid Johansson was born on November 22, 1984 in Manhattan, New York City, New York. Her mother, Melanie Sloan is from a Jewish family from the Bronx and her father, Karsten Johansson is a Danish-born architect from Copenhagen. She has a sister, Vanessa Johansson, who is also an actress, a brother, Adrian, a twin brother, Hunter Johansson

"""
)




with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(
Robert_DowneyJr )
        #yes
    with text_column:
         st.header("Robert_DowneyJr ")
         st.write(
"""
Robert Downey Jr. has evolved into one of the most respected actors in Hollywood. With an amazing list of credits to his name, he has managed to stay new and fresh even after over four decades in the business. Downey was born April 4, 1965 in Manhattan, New York, the son of writer, director and filmographer Robert Downey Sr. 


"""
)


      
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Christopher_Hemsworth)
        #yes
    with text_column:
         st.header("Christopher_Hemsworth")
         st.write(
"""
 Christopher Hemsworth was born on August 11, 1983 in Melbourne, Victoria, Australia to Leonie Hemsworth (née van Os), an English teacher & Craig Hemsworth, a social-services counselor. His brothers are actors, Liam Hemsworth & Luke Hemsworth; he is of Dutch (from his immigrant maternal grandfather), Irish, English, Scottish, and German ancestry.
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Mark_Ruffalo)
        #yes
    with text_column:
         st.header("Mark_Ruffalo")
         st.write(
"""
 Award-winning actor Mark Ruffalo was born on November 22, 1967, in Kenosha, Wisconsin, of humble means to father Frank Lawrence Ruffalo, a construction painter and Marie Rose (Hebert), a stylist and hairdresser; his father's ancestry is Italian and his mother is of half French-Canadian and half Italian descent
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Salma_Hayek)
        #yes
    with text_column:
         st.header("Salma_Hayek")
         st.write(
"""
 Salma Hayek was born on September 2, 1966 in Coatzacoalcos, Mexico. Her father is of Lebanese descent and her mother is of Mexican/Spanish ancestry. After having seen Willy Wonka & the Chocolate Factory (1971) in a local movie theater, she decided she wanted to become an actress. At age 12, she was sent to the Academy of the Sacred Heart
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Angelina_Jolie)
        #yes
    with text_column:
         st.header("Angelina_Jolie")
         st.write(
"""
 Angelina Jolie is an Academy Award-winning actress who rose to fame after her role in Girl, Interrupted (1999), playing the title role in the "Lara Croft" blockbuster movies, as well as Mr. & Mrs. Smith (2005), Wanted (2008), Salt (2010) and Maleficent (2014). Off-screen, Jolie has become prominently involved in international charity projects
 """
)
    
   
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Tom_Hardy)
        #yes
    with text_column:
         st.header("Tom_Hardy")
         st.write(
"""
 With his breakthrough performance as Eames in Christopher Nolan's sci-fi thriller Inception (2010), English actor Tom Hardy has been brought to the attention of mainstream audiences worldwide. However, the versatile actor has been steadily working on both stage and screen since his television debut in the miniseries Band of Brothers (2001)
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Gemma_Chan)
        #yes
    with text_column:
         st.header("Gemma_Chan")
         st.write(
"""
 Gemma Chan (born 29 November 1982) is a British film, television, and theatre actress and former fashion model. She played Charlotte in season four of the Showtime and ITV2 series Secret Diary of a Call Girl (2007); Ruth in Channel 4's Fresh Meat (2011); Mia Bennett in Doctor Who: The Waters of Mars (2009), and Soo Lin in Sherlock: The Blind Banker
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Tom_Holland)
        #yes
    with text_column:
         st.header("Tom_Holland")
         st.write(
"""
 homas Stanley Holland was born in Kingston-upon-Thames, Surrey, to Nicola Elizabeth (Frost), a photographer, and Dominic Holland (Dominic Anthony Holland), who is a comedian and author. His paternal grandparents were from the Isle of Man and Ireland, respectively. He lives with his parents and three younger brothers - Paddy and twins Sam
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Paul_Rudd)
        #yes
    with text_column:
         st.header("Paul_Rudd")
         st.write(
"""
 Paul Stephen Rudd was born in Passaic, New Jersey. His parents, Michael and Gloria, both from Jewish families, were born in the London area, U.K. He has one sister, who is three years younger than he is. Paul traveled with his family during his early years, because of his father's airline job at TWA. His family eventually settled in Overland Park
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Benedict_Cumberbatch)
        #yes
    with text_column:
         st.header("Benedict_Cumberbatch")
         st.write(
"""
 Benedict Timothy Carlton Cumberbatch was born and raised in London, England. His parents, Wanda Ventham and Timothy Carlton (born Timothy Carlton Congdon Cumberbatch), are both actors. He is a grandson of submarine commander Henry Carlton Cumberbatch, and a great-grandson of diplomat Henry Arnold Cumberbatch CMG. 
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Paul_Bettany)
        #yes
    with text_column:
         st.header("Paul_Bettany")
         st.write(
"""
 Paul Bettany is an English actor. He first came to the attention of mainstream audiences when he appeared in the British film Gangster No. 1 (2000), and director Brian Helgeland's film A Knight's Tale (2001). He has gone on to appear in a wide variety of films, including A Beautiful Mind (2001), Master and Commander: The Far Side of the World
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Donald_Frank_Cheadle)
        #yes
    with text_column:
         st.header("Donald_Frank_Cheadle")
         st.write(
"""
 Donald Frank Cheadle was born in Kansas City, Missouri, on November 29, 1964. His childhood found him moving from city to city with his family: mother Bettye (née North), a teacher; father Donald Frank Cheadle Sr., a clinical psychologist; sister Cindy; and brother Colin. After graduating from high school in Denver, Colorado, Cheadle attended 
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Thomas_William_Hiddleston)
        #yes
    with text_column:
         st.header("Thomas_William_Hiddleston")
         st.write(
"""
 Thomas William Hiddleston was born in Westminster, London, to English-born Diana Patricia (Servaes) and Scottish-born James Norman Hiddleston. His mother is a former stage manager, and his father, a scientist, was the managing director of a pharmaceutical company. He started off at the preparatory school, The Dragon School in Oxford
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Sebastian_Stan)
        #yes
    with text_column:
         st.header("Sebastian_Stan")
         st.write(
"""
 Sebastian Stan was born on August 13, 1982, in Constanta, Romania. He moved with his mother to Vienna, Austria, when he was eight, and then to New York when he was twelve. Stan studied at Rutgers Mason Gross School of the Arts and spent a year at Shakespeare's Globe Theatre in London.
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Jeremy_Renner)
        #yes
    with text_column:
         st.header("Jeremy_Renner")
         st.write(
"""
 Jeremy Lee Renner was born in Modesto, California, the son of Valerie (Tague) and Lee Renner, who managed a bowling alley. After a tumultuous yet happy childhood with his four younger siblings, Renner graduated from Beyer High School and attended Modesto Junior College. He explored several areas of study, including computer science, criminology
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Elizabeth_Olsen )
        #yes
    with text_column:
         st.header("Elizabeth_Olsen ")
         st.write(
"""
 Elizabeth Chase "Lizzie" Olsen (born February 16, 1989) is an American actress. She is known for her roles in the films Silent House (2011), Liberal Arts (2012), Godzilla (2014), Avengers: Age of Ultron (2015), and Captain America: Civil War (2016). For her role in the critically-acclaimed Martha Marcy May Marlene (2011), she was nominated for numerous awards, including the Independent Spirit Award for Best Female Lead.
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Tessa_Thompson)
        #yes
    with text_column:
         st.header("Tessa_Thompson")
         st.write(
"""
The actress Tessa Lynn Thompson was born on October 3, 1983 in Los Angeles, California. She is the daughter of singer-songwriter Marc Anthony Thompson and the granddaughter of actor-musician Bobby Ramos. She was raised in Los Angeles before moving to Brooklyn, New York. Her father is of Afro-Panamanian ancestry and her mother is of Mexican and British Isles ancestry.
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Letitia_Michelle_Wright)
        #yes
    with text_column:
         st.header("Letitia_Michelle_Wright")
         st.write(
"""
 With a career spanning over a decade, Emmy-nominated Letitia Wright has cemented her position as one of the industry's most captivating young actresses. From her breakout role as ambitious Summerhouse resident Chantelle in Top Boy, to her critically acclaimed performance as Nish in Black Mirror
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Jamie_Foxx)
        #yes
    with text_column:
         st.header("Jamie_Foxx")
         st.write(
"""
 Jamie Foxx is an American actor, singer and comedian. He won an Academy Award for Best Actor, BAFTA Award for Best Actor in a Leading Role, and Golden Globe Award for Best Actor in a Musical or Comedy, for his work in the biographical film Ray (2004). The same year, he was nominated for the Academy Award for Best Supporting Actor
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Jake_Gyllenhaal )
        #yes
    with text_column:
         st.header("Jake_Gyllenhaal ")
         st.write(
"""Jacob Benjamin Gyllenhaal was born in Los Angeles, California, to producer/screenwriter Naomi Foner (née Achs) and director Stephen Gyllenhaal. He is the brother of actress Maggie Gyllenhaal, who played his sister in Donnie Darko (2001). His godmother is actress Jamie Lee Curtis. His mother is from a Jewish family
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Richard_Madden)
        #yes
    with text_column:
         st.header("Richard_Madden")
         st.write(
"""
 Richard Madden, born 18 June 1986, is a Scottish stage, film, and television actor best known for portraying Robb Stark in the HBO series "Game of Thrones" and Prince Kit in Disney's "Cinderella." Starring as David Budd in the BBC miniseries "Bodyguard" has also brought him more international acclaim and attention including a Golden Globe
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(
Benedict_Wong)
        #yes
    with text_column:
         st.header("Benedict_Wong")
         st.write(
"""
 Benedict Wong was born on February 20, 1970 in Eccles, England. He is an actor and writer, known for Annihilation (2018), Doctor Strange (2016) and Avengers: Infinity War (2018).
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Chris_Pratt)
        #yes
    with text_column:
         st.header("Chris_Pratt")
         st.write(
"""
 Christopher Michael "Chris" Pratt was born on June 21, 1979 in Virginia, Minnesota and raised in Lake Stevens, Washington to Kathleen Louise Pratt (née Indahl), who worked at a supermarket & Daniel Clifton Pratt, who remodeled houses. He is of mostly Norwegian descent. He graduated from Lake Stevens High School in 1997, and has two older siblings
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Zoe_Saldana)
        #yes
    with text_column:
         st.header("Zoe_Saldana")
         st.write(
"""
 Zoe Saldana was born on June 19, 1978 in Passaic, New Jersey, to Asalia Nazario and Aridio Saldaña. Her father was Dominican and her mother is Puerto Rican. She was raised in Queens, New York. When she was 10 years old, she and her family moved to the Dominican Republic, where they would live for the next seven years
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Krysten_Ritter)
        #yes
    with text_column:
         st.header("Krysten_Ritter")
         st.write(
"""
 Krysten Alyce Ritter is an American actress and model. She came to prominence when she appeared as Jane Margolis in the AMC drama series Breaking Bad and its spinoff film El Camino
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Karen_Gillan)
        #yes
    with text_column:
         st.header("Karen_Gillan")
         st.write(
"""
 Karen Sheila Gillan was born and raised in Inverness, Scotland, as the only child of Marie Paterson and husband John Gillan, who is a singer and recording artist. She developed a love for acting very early on, attending several youth theatre groups and taking part in a wide range of productions at her school, Charleston Academy.
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Brie_LarsonC)
        #yes
    with text_column:
         st.header("Brie_LarsonC")
         st.write(
"""
 Brie Larson has built an impressive career as an acclaimed television actress, rising feature film star and emerging recording artist. A native of Sacramento, Brie started studying drama at the early age of 6, as the youngest student ever to attend the American Conservatory Theater in San Francisco
 """
)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Anthony_Dwane_Mackie)
        #yes
    with text_column:
         st.header("Anthony_Dwane_Mackie")
         st.write(
"""
 Anthony Mackie is an American actor. He was born in New Orleans, Louisiana, to Martha (Gordon) and Willie Mackie, Sr., who owned a business, Mackie Roofing. Anthony has been featured in feature films, television series and Broadway and Off-Broadway plays, including Ma Rainey's Black Bottom, Drowning Crow, McReele, A Soldier's Play
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Barry_Keoghan )
        #yes
    with text_column:
         st.header("Barry_Keoghan ")
         st.write(
"""
 Barry came to prominence in the 2017 film 'The Killing of a Sacred Deer' with his truly terrifying portrayal of Martin,an American teenager exacting a grisly revenge on drunken surgeon Colin Farrell, but he was not an American nor a teen-ager, born in Dublin on 17th October 1992 and has a brother Eric.
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Alfred_Molina)
        #yes
    with text_column:
         st.header("Alfred_Molina")
         st.write(
"""
 Alfred Molina was born in 1953 in London, England. His mother, Giovanna (Bonelli), was an Italian-born cook and cleaner, and his father, Esteban Molina, was a Spanish-born waiter and chauffeur. He studied at the Guildhall School of Music and Drama, London.
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Willem_Dafoe)
        #yes
    with text_column:
         st.header("Willem_Dafoe")
         st.write(
"""
Having made over one hundred films in his legendary career, Willem Dafoe is internationally respected for bringing versatility, boldness, and daring to some of the most iconic films of our time. His artistic curiosity in exploring the human condition leads him to projects all over the world, large and small, Hollywood
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Tobey_Maguire )
        #yes
    with text_column:
         st.header("Tobey_Maguire ")
         st.write(
"""
Tobias Vincent Maguire was born in Santa Monica, California. His parents were 18 and 20, and not yet married, when he was born. His mother, Wendy (Brown), did advertising, publicity, and acting in Hollywood for years as she coached and managed Tobey. His father, Vincent Maguire, was a cook and sometimes a construction worker.
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Andrew_Garfield)
        #yes
    with text_column:
         st.header("Andrew_Garfield")
         st.write(
"""
 Andrew Russell Garfield was born in Los Angeles, California, to a British mother, Lynn, and American father, Richard Garfield. When he was three, he moved to Surrey, U.K., with his parents and older brother. He is of English and Polish Jewish heritage. Andrew was raised in a middle class family, and attended a private school, the City of London
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Samuel_LJackson)
        #yes
    with text_column:
         st.header("Samuel_LJackson")
         st.write(
"""
 Samuel L. Jackson is an American producer and highly prolific actor, having appeared in over 100 films, including Die Hard with a Vengeance (1995), Unbreakable (2000), Shaft (2000), Formula 51 (2001), Black Snake Moan (2006), Snakes on a Plane (2006), and the Star Wars prequel trilogy (1999-2005), as well as the Marvel Cinematic Universe
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Kumail_Nanjiani)
        #yes
    with text_column:
         st.header("Kumail_Nanjiani")
         st.write(
"""
 Kumail Nanjiani is an actor and writer, known for The Big Sick (2017), Life as We Know It (2010) and Stuber (2019). He has been married to Emily V. Gordon since July 14, 2007.
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Lauren_Ridloff )
        #yes
    with text_column:
         st.header("Lauren_Ridloff ")
         st.write(
"""
 Lauren Ridloff is an American actress and former teacher. She is known as a former Miss Deaf America (2000 - 2002), as Lauren Teruel. She's also known for her 2018 Tony-nominated Broadway performance as Sarah Norman in Children of a Lesser God, and as Connie in the AMC Television series The Walking Dead.
 """
)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Chadwick_Boseman )
        #yes
    with text_column:
         st.header("Chadwick_Boseman ")
         st.write(
"""
 Chadwick Boseman was an American actor. He is known for his portrayal of T'Challa / Black Panther in the Marvel Cinematic Universe from 2016 to 2019, particularly in Black Panther (2018), and for his starring roles as several pioneering Americans, Jackie Robinson in 42 (2013), James Brown in Get on Up (2014), and Thurgood Marshall in Marshall
 """
)



with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Hayley_Elizabeth_Atwell)
        #yes
    with text_column:
         st.header("Hayley_Elizabeth_Atwell")
         st.write(
"""
 Born in London, England, Hayley Elizabeth Atwell has dual citizenship of the United Kingdom and the United States. An only child, Hayley was named after actress Hayley Mills. Her parents, Alison (Cain) and Grant Atwell, both motivational speakers, met at a London workshop of Dale Carnegie's self-help bible "How to Win Friends
 """
)