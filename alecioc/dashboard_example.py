import os
import streamlit as st
from PIL import Image
import pandas as pd
from youtubesearchpython import VideosSearch


st.set_page_config(
    page_title="STEM days",
    page_icon=Image.open(os.path.join("images", "stem_days_logo.png")),
    layout='wide',
    initial_sidebar_state='auto'
)

st.sidebar.title("Menu laterale")
st.sidebar.subheader("Qui potremmo inserire una modalità semplice di navigazione")

sidebar_page = st.sidebar.selectbox(
    "Seleziona pagina corrente:",
    [
        "Home",
        "Pagina 1",
        "Pagina 2",
        "Pagina 3",
    ]
)

# Simple menu

if sidebar_page == "Home":

    # Modo facile di scrivere testo su streamlit
    st.title("Webby")
    st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

    # Modo "difficile" (HTML+CSS) di scrivere testo su streamlit
    original_title = """
        <p style="font-family:Courier; color:Blue; font-size: 20px;">
            A custom style in HTML+CSS
        </p>    
    """
    st.markdown(original_title, unsafe_allow_html=True)
    new_title = """
        <p style="font-family:sans-serif; color:Green; font-size: 42px;">
            Another custom style in HTML+CSS
        </p>
    """
    st.markdown(new_title, unsafe_allow_html=True)

    # Immagine
    st.image(Image.open(os.path.join("images", "stemdays-social.jpeg")))

elif sidebar_page == "Pagina 1":
    # Tabella
    df = pd.read_csv(os.path.join("data", "10k_random_tracks.csv"), index_col=0)
    st.header("Inserire una tabella (dataframe)")
    st.subheader("Qui inseriamo una tabella con 10000 canzoni in forma larga")
    st.write(df.shape)
    st.dataframe(df)
    st.subheader("Qui inseriamo una tabella con 10000 canzoni in forma lunga")
    df_long = df.melt("name", var_name="column", value_name="value")
    st.write(df_long.shape)
    st.dataframe(df_long)

elif sidebar_page == "Pagina 2":
    st.header("Inserire un video da youtube")
    st.subheader("Qui recuperiamo il link Youtube della prima canzone nel dataset")
    st.subheader("Sarebbe carino fare un menu a tendina di selezione")
    df = pd.read_csv(os.path.join("data", "10k_random_tracks.csv"), index_col=0)
    # Questo serve per convertire le colonne che dovrebbero essere di tipo lista ma vengono lette come stringhe dal csv
    # Magari wrappiamo alcune di queste robe e gliele diamo se servono
    # (per esempio riconoscere artisti diversi in un featuring)
    from ast import literal_eval
    df.artists = df.artists.apply(literal_eval)
    name_and_artists_string = " ".join([df.iloc[0]["name"]] + [artist for artist in df.iloc[0]["artists"]])
    st.subheader(name_and_artists_string)
    videosSearch = VideosSearch(
        name_and_artists_string,
        limit=1
    )
    st.write(videosSearch.result()["result"][0]["link"])
    st.video(videosSearch.result()["result"][0]["link"])

elif sidebar_page == "Pagina 3":

    st.header("Grafico interattivo Altair")
    st.subheader("Possiamo preimpostare funzioni tipo codice sotto")
    st.subheader("Se mettiamo i dati in long form, Altair risulta molto carino")
    st.subheader("Possiamo farlo nascondendo alle ragazze questa complessità")

    df = pd.read_csv(os.path.join("data", "10k_random_tracks.csv"), index_col=0)
    artists_selected = st.selectbox(
        "Seleziona artista o gruppo:",
        df.artists.values
    )
    selected_artist_df = df[
        df.artists == artists_selected
    ][["name", "popularity"]].copy()
    df_long = selected_artist_df.melt("name", var_name="column", value_name="popularity")
    st.write(df_long)

    import altair as alt
    bars = alt.Chart(df_long).mark_bar().encode(
        x="popularity:Q",
        y='name:O',
        tooltip=['name', 'popularity']
    )
    st.altair_chart(bars, use_container_width=True)
