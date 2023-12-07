import streamlit as st

st.title("About")

from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("April Evan Jean Y. Elico")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:

    st.write("Hi!I'm April Evan Jean Y. Elico, 18 years of age. I am quite shy and uncomfortable around new people, but does the craziest things with people I feel comfortable with. I hate social gatherings and I don't like crowded places becauase I get anxious easily. I like drawing and playing the guitar, as well as listening to music during my free time.")