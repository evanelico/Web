import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave",

)

st.sidebar.success("Select a page above.")

from PIL import Image
import requests

import streamlit as st
#from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("Evan's Blog :penguin:")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Hi, I'm April Evan Jean Y. Elico")
    st.subheader("A BSCpE student from SNSU main campus.")
    
    st.subheader("These are my socials, feel free to visit them.")
    st.write(" ▶ Facebook: https://www.facebook.com/aprilevanjean.elico.1")
    st.write(" ▶Email: elicoevan.gmail@com")
    st.write(" ▶Contact Number: 09075301770")
