import streamlit as st

st.title("Others")

from PIL import Image
import requests

import streamlit as st
#from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("La Familia")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/9.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("This is my fam.")
    st.write("They are the most significant people in my life. They've been with me ever since I came out of this world. We fight a lot, but that's just how we show our love for one another, besides, it's normal for families to fight even in small things.")
    
st.title("Mother")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/4.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Evette Y. Elico")
    st.write("My mother can come out as a sweet and loving individual, but can also be strict and fierce when needed. She may look like she doesn't care with the people around her, but I know deep down that she's the very first person who you can come to whenever something goes wrong. She's not showy, and she does not express her feelings that much, but you can tell that she loves you through her actions. My mother has been through a lot of things, but she never gave up, and I admire her for that.")
    
st.title("Father")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/3.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Jeyson T. Elico")
    st.write("He is the coolest, funniest, and caring person I've ever known. The one who you can always rely on, my father. Though he is kind and loving, some people's perception of him is still scary and unkind, when the truth is he is the exact opposite of what they actually perceive him. My father has made a lot of sacrifices for our family, and I admire him for all that. He's the one who puts food on our table, and we wouldn't be able to survive each passing day without him. The word grateful wouldn't be enough to describe how thankful I am to have him as my father.")    

st.title("Little Sis")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/2.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Jeyanna Venesse Y. Elico")
    st.write("Meet my little sister, Jeyanna Venesse Y. Elico, she was born on the 19th of March. A 3 years old child who's beautiful, sweet, and loving. Many people like her because she's not like other kids. She can already speak without stuttering, and she talks like how elders talk due to the fact that our grandmother is the one who's taking care of her. They say that she's the exact opposite of me, and I totally agree.")

st.title("Second Fam")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/5.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.write("They are the people whom I consider as my second family. They're the ones who took care of me when my parents are not around. They always make me feel welcome in their home. When I was little, I used to come to their house just to play with my younger cousin because she don't have someone else to play with, and our house are just a few meters away with one another so we can play and talk whenever we want.")    

st.title("Friends")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/6.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("My Friends in Senior High School")
    st.write("Even though we don't see each other that much nowadays due to busy schedule, we still keep in touch through messenger and our other social media accounts. We made a lot of memories back then. We used to go to different places during our free time, and it was really wonderful spending time with them. To me, those times were the most memorable day of my life, and I hope that I could get to spend time with them again in the future. ")

st.title("My Friends in College")    

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/7.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/8.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)    

with text_column:

   st.write("These are my friends now. We easily get along and treated each other as family. We always help each other out, because we have such mindset that we cannot survive college when all we do is compete and drag each other down. I will forever thank God for letting me meet these wonderful people, because even though we only spend time together for a short period of time, they made me feel the happiest. I hope that this friendship will last for a lifetime.")    