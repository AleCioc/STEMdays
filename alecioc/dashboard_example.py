import os
import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(
    page_title="STEM days",
    page_icon=Image.open(os.path.join("images", "stem_days_logo.png")),
    layout='wide',
    initial_sidebar_state='auto'
)

st.title("Webby")
st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">A custom style in HTML+CSS</p>'
st.markdown(original_title, unsafe_allow_html=True)

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Another custom style in HTML+CSS</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.sidebar.title("Menu laterale")
st.sidebar.subheader("Qui potremmo inserire una modalità semplice di navigazione")

sidebar_page = st.sidebar.selectbox(
    "Seleziona pagina corrente:",
    ["Home", "Pagina 1"]
)

if sidebar_page == "Home":
    st.image(Image.open(os.path.join("images", "stemdays-social.jpeg")))

elif sidebar_page == "Pagina 1":
    st.header("Inserire una tabella")
    st.subheader("Qui inseriamo una tabella con 10000 canzoni")

    df = pd.read_csv(os.path.join("data", "10k_random_tracks.csv"))
    st.dataframe(df)
