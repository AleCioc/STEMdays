import streamlit as st

st.set_page_config(
    page_title="TITOLO",
    page_icon=None,
    layout='wide',
    initial_sidebar_state='auto'
)

st.sidebar.title("Menu laterale")
st.sidebar.subheader("Qui possiamo inserire una modalità semplice di navigazione")

sidebar_page = st.sidebar.selectbox(
    "Seleziona pagina corrente:",
    ["Home", "Pagina 1", "Il nostro Team"]
)

if sidebar_page == "Home":

    # Modo facile di scrivere testo su streamlit
    st.title("Webby")
    st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

elif sidebar_page == "Pagina 1":

    # Modo facile di scrivere testo su streamlit
    st.title("Pagina 1")
    st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

elif sidebar_page == "Il nostro Team":

    # Modo facile di scrivere testo su streamlit
    st.title("Il nostro Team")
    st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")



