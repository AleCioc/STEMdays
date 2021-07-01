from youtubesearchpython import VideosSearch
from ast import literal_eval
import os
import geopandas as gpd
import plotly.express as px

import pandas as pd
import streamlit as st
import plotly.express as px
import wikipedia
from musixmatch import Musixmatch
from ast import literal_eval
import webbrowser


st.set_page_config(
    page_title="Webby",
    page_icon="https://www.stemdays.it/img/StemDays-Torino-Camp-contattaci.png",
    layout='wide',
    initial_sidebar_state='auto'
)

st.sidebar.title("Menu laterale")
st.sidebar.subheader("Qui possiamo inserire una modalità semplice di navigazione")

sidebar_page = st.sidebar.selectbox(
    "Seleziona pagina corrente:",
    ["Home", "Gallery", "Testo", "Accordi", "Grafici", "Bio artisti", "Tendenze del mondo", "Il nostro Team"])

if sidebar_page == "Home":
    st.markdown(
        """ 
        <style> 
        .reportview-container { 
            background: url("https://3.bp.blogspot.com/-epYx5YUHxac/WKRYKR1-dlI/AAAAAAAAA44/vklK0_ynIEcThtCBCy4lxtmqcfSVteXVQCLcB/s1600/music%2Bgif%2B1.gif") 
        } 
       .sidebar .sidebar-content { 
            background: url("url_goes_here") 
        } 
        </style> 
        """,
        unsafe_allow_html=True
    )

    st.title("Benvenutə")

    st.header("Questo è il nostro sito.")
    st.subheader("Usa il menu a sinistra per navigare.")

    # Modo facile di scrivere testo su streamlit

    st.write("Qui sotto c'è una breve spiegazione di tutte le pagine:")

    colonna1, colonna2 = st.beta_columns(2)

    expander = colonna1.beta_expander("Gallery")
    expander.write(
        "Attraverso questa rubrica riuscirete ad ascoltare tutti i brani che abbiamo selezionato per voi")

    expander = colonna1.beta_expander("Testo")
    expander.write("Questa funzione ti permette di avere a disposizione il testo delle canzoni selezionate")

    expander = colonna1.beta_expander("Accordi")
    expander.write("20 canzoni selezionate per te da suonare")

    expander = colonna1.beta_expander("Grafici")
    expander.write("Avrai a disposizione diversi grafici per analizzare la musica")

    expander = colonna1.beta_expander("Bio Artisti")
    expander.write("Tutte le informazioni necessarie di ogni artista a disposizione con un click")

    expander = colonna1.beta_expander("Tendenze del mondo")
    expander.write("Scoprirai quali sono le canzone più ascoltate nei vari paesi del mondo")

    expander = colonna1.beta_expander("Il nostro Team")
    expander.write("Scopri più informazioni su di noi")

elif sidebar_page == "Gallery":

    colonna1, colonna2 = st.beta_columns((4, 2))

    colonna1.title("Gallery")
    colonna1.header("Qui puoi vedere i video delle canzoni disponibili")


    df = pd.read_csv(os.path.join("10k_random_tracks.csv"), index_col=0)
    # Prendere solo le prime 100 colonne del dataframe per renderlo piu' veloce
    df = df.iloc[:100]
    # Questo serve per convertire le colonne che dovrebbero essere di tipo lista ma vengono lette come stringhe dal csv
    # Magari wrappiamo alcune di queste robe e gliele diamo se servono
    # (per esempio riconoscere artisti diversi in un featuring)
    option = colonna2.selectbox("Scegli la canzone: ", df.name.values)
    df.artists = df.artists.apply(literal_eval)
    riga = df[df.name == option].iloc[0]
    name_and_artists_string = " ".join([riga["name"]] + [artist for artist in riga["artists"]])
    colonna2.header("Canzone scelta")
    colonna2.subheader(name_and_artists_string)
    videosSearch = VideosSearch(
        name_and_artists_string,
        limit=1
    )
    if videosSearch.result()["result"]:
        colonna1.write(videosSearch.result()["result"][0]["link"])
        colonna1.video(videosSearch.result()["result"][0]["link"])
    else:
        colonna1.write("Video unavailable")

elif sidebar_page == "Testo":
    st.title("Testo")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

    df = pd.read_csv("10k_random_tracks.csv", index_col=0)
    df.artists = df.artists.apply(literal_eval)
    expander = st.beta_expander("Tabella totale parametri.")
    expander.dataframe(df)
    # st.selectbox("Seleziona Artista", df.artists.values)
    artista_selezionato = st.selectbox("Seleziona artista", df.artists.values)
    df_artista = df[df.artists.apply(lambda x: x[0]) == artista_selezionato[0]]
    st.dataframe(df_artista)
    canzone = st.selectbox("Seleziona canzone", df_artista.name.values)
    riga = df[df.name == canzone].iloc[0]
    artista1 = riga.artists[0]

    mxm = Musixmatch('d63448247d144f22f2bfc15d5bfc58ba')
    track_response = mxm.track_search(
        q_artist=artista_selezionato,
        q_track=canzone,
        page_size=10, page=1, s_track_rating='desc'
    )

    if len(track_response["message"]["body"]["track_list"]) > 0:
        track_id = track_response["message"]["body"]["track_list"][0]["track"]["track_id"]
        if mxm.track_lyrics_get(track_id)["message"]["header"]["status_code"] == 200:
            testo = mxm.track_lyrics_get(track_id)["message"]["body"]["lyrics"]["lyrics_body"]
            st.write(testo)
        else:
            st.error("Il testo di questa canzone non è stato trovato. Scusate.")
    else:
        st.error("Il testo di questa canzone non è stato trovato. Scusate.")

elif sidebar_page == "Accordi":
    st.markdown(
        """ 
        <style> 
        .reportview-container {  
            background-image: url("https://stonemusic.it/wp-content/uploads/2018/11/vinile_HD.jpg");
            background-size: cover;
        } 
       .sidebar .sidebar-content { 
            background: url("url_goes_here") 
        } 
        </style> 
        """,
        unsafe_allow_html=True
    )

    st.markdown('<style>h1{text-shadow: 2px 2px #31333F;}</style>', unsafe_allow_html=True)
    st.write("<h1>Accordi</h1>", unsafe_allow_html=True)

    ciao1, ciao2, ciao3 = st.beta_columns((2, 4, 2))

    st.markdown('<style>h2{text-shadow: 2px 2px #31333F;}</style>', unsafe_allow_html=True)
    ciao2.write("<h2>Repertorio</h2>", unsafe_allow_html=True)

    ciao1.image("ukulele.gif")

    ciao3.image("note.gif")

    ciao2.markdown('<style>h6{text-shadow: 2px 2px #31333F;}</style>', unsafe_allow_html=True)
    ciao2.write("<h6>Questi sono gli artisti cha abbiamo selezionato per voi</h6>", unsafe_allow_html=True)

    expander = ciao2.beta_expander("Aloe Blacc")
    if expander.button("I need a dollar"):
        expander.write("https://tabs.ultimate-guitar.com/tab/aloe-blacc/i-need-a-dollar-chords-940222")
    
    expander = ciao2.beta_expander("Arctic Monkeys")
    if expander.button("I wanna be yours"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/arctic-monkeys/i-wanna-be-yours-chords-1417191")
    
    expander = ciao2.beta_expander("Ariana Grande")
    if expander.button("The way"):
        expander.write("https://tabs.ultimate-guitar.com/tab/ariana-grande/the-way-chords-1242015")
    
    expander = ciao2.beta_expander("Avril Lavigne")
    if expander.button("When you're gone"):
        expander.write("https://tabs.ultimate-guitar.com/tab/avril-lavigne/when-youre-gone-chords-476244")
    
    expander = ciao2.beta_expander("Billie Eilish")
    if expander.button("Everything I wanted"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/billie-eilish/everything-i-wanted-chords-2892650")
    
    expander = ciao2.beta_expander("Bruce Springsteen")
    if expander.button("The rising"):
        expander.write("https://tabs.ultimate-guitar.com/tab/bruce-springsteen/the-rising-chords-1088613")
    
    expander = ciao2.beta_expander("Bruno Mars")
    if expander.button("It will rain"):
        expander.write("https://tabs.ultimate-guitar.com/tab/bruno-mars/it-will-rain-chords-1096050")
    
    expander = ciao2.beta_expander("Calcutta")
    if expander.button("Frosinone"):
        expander.write("https://tabs.ultimate-guitar.com/tab/calcutta/frosinone-chords-1800785")
    
    expander = ciao2.beta_expander("Calvin Harris")
    if expander.button("Summer"):
        expander.write("https://tabs.ultimate-guitar.com/tab/calvin-harris/summer-chords-1469858")
    
    expander = ciao2.beta_expander("Cristina Aguilera")
    if expander.button("Genie in a bottle"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/christina-aguilera/genie-in-a-bottle-chords-1193224")
    
    expander = ciao2.beta_expander("Ed Sheeran")
    if expander.button("Sing"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/christina-aguilera/genie-in-a-bottle-chords-1193224")

    expander = ciao2.beta_expander("Edith Whiskers")
    if expander.button("Home"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/christina-aguilera/genie-in-a-bottle-chords-1193224")
    
    expander = ciao2.beta_expander("Ella Fitzgerald")
    if expander.button("Let's fall in love"):
        expander.write("https://tabs.ultimate-guitar.com/tab/finneas/lets-fall-in-love-for-the-night-chords-2549901")

    expander = ciao2.beta_expander("Eric Clapton")
    if expander.button("Running on faith"):
        expander.write("https://tabs.ultimate-guitar.com/tab/eric-clapton/running-on-faith-chords-63608")

    expander = ciao2.beta_expander("Etta James")
    if expander.button("At last"):
        expander.write("https://tabs.ultimate-guitar.com/tab/etta-james/at-last-chords-813094")

    expander = ciao2.beta_expander("Fitz and the Tantrums")
    if expander.button("Out of my league"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/fitz-and-the-tantrums/out-of-my-league-chords-1401040")

    expander = ciao2.beta_expander("Gloria Gaynor")
    if expander.button("I will survive"):
        expander.write("https://tabs.ultimate-guitar.com/tab/gloria-gaynor/i-will-survive-chords-991389")

    expander = ciao2.beta_expander("Green Day")
    if expander.button("Having a blast"):
        expander.write("https://tabs.ultimate-guitar.com/tab/green-day/having-a-blast-chords-1095148")

    if expander.button("Oh love"):
        expander.write("https://tabs.ultimate-guitar.com/tab/green-day/oh-love-chords-1169046")

    expander = ciao2.beta_expander("Guns N' Roses")
    if expander.button("Sweet child o' mine"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/guns-n-roses/sweet-child-o-mine-chords-176076")

    expander = ciao2.beta_expander("Halsey")
    if expander.button("New americana"):
        expander.write("https://tabs.ultimate-guitar.com/tab/halsey/new-americana-chords-1729709")

    if expander.button("Without me"):
        expander.write("https://tabs.ultimate-guitar.com/tab/halsey/without-me-chords-2485194")

    expander = ciao2.beta_expander("Imagine dragons")
    if expander.button("On top of the world"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/imagine-dragons/on-top-of-the-world-chords-1164788")

    expander = ciao2.beta_expander("Justin Bieber")
    if expander.button("Love yourself"):
        expander.write("https://tabs.ultimate-guitar.com/tab/justin-bieber/love-yourself-chords-1780199")

    expander = ciao2.beta_expander("Kanye West")
    if expander.button("Hell of a life"):
        expander.write("https://tabs.ultimate-guitar.com/tab/kanye-west/hell-of-a-life-tabs-1465911")

    if expander.button("Stronger"):
        expander.write("https://tabs.ultimate-guitar.com/tab/kanye-west/stronger-chords-566584")

    expander = ciao2.beta_expander("Lady Gaga")
    if expander.button("The edge of glory"):
        expander.write("https://tabs.ultimate-guitar.com/tab/lady-gaga/the-edge-of-glory-chords-1055910")

    expander = ciao2.beta_expander("Lana del rey")
    if expander.button("Pretty when you cry"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/lana-del-rey/pretty-when-you-cry-chords-1493667")

    expander = ciao2.beta_expander("Lil Peep")
    if expander.button("Falling down"):
        expander.write("https://tabs.ultimate-guitar.com/tab/lil-peep/falling-down-chords-2475082")

    expander = ciao2.beta_expander("Maroon 5")
    if expander.button("One more night"):
        expander.write("https://tabs.ultimate-guitar.com/tab/maroon-5/one-more-night-chords-1164814")

    expander = ciao2.beta_expander("Nirvana")
    if expander.button("Lithium"):
        expander.write("https://tabs.ultimate-guitar.com/tab/nirvana/lithium-chords-1119299")

    expander = ciao2.beta_expander("Oasis")
    if expander.button("Sunday morning call"):
        expander.write("https://tabs.ultimate-guitar.com/tab/oasis/sunday-morning-call-chords-6080")

    expander = ciao2.beta_expander("Ozuna")
    if expander.button("Baila baila baila"):
        expander.write("https://tabs.ultimate-guitar.com/tab/ozuna/baila-baila-baila-chords-2566122")

    expander = ciao2.beta_expander("Pink Floyd")
    if expander.button("Money"):
        expander.write("https://tabs.ultimate-guitar.com/tab/pink-floyd/money-chords-43461")

    expander = ciao2.beta_expander("Queen")
    if expander.button("Another one lights the dust"):
        expander.write("https://tabs.ultimate-guitar.com/tab/queen/another-one-bites-the-dust-chords-1090617")

    expander = ciao2.beta_expander("Raffaella Carrà")
    if expander.button("Tanti Auguri"):
        expander.write("https://tabs.ultimate-guitar.com/tab/1727358")

    expander = ciao2.beta_expander("Rihanna")
    if expander.button("California king bed"):
        expander.write("https://tabs.ultimate-guitar.com/tab/rihanna/california-king-bed-chords-1057199")

    if expander.button("What's my name"):
        expander.write("https://tabs.ultimate-guitar.com/tab/rihanna/whats-my-name-chords-1020630")

    expander = ciao2.beta_expander("Slipknot")
    if expander.button("Psychosocial"):
        expander.write("https://tabs.ultimate-guitar.com/tab/slipknot/psychosocial-chords-744228")

    expander = ciao2.beta_expander("Taylor Swift")
    if expander.button("I knew you were trouble"):
        expander.write(
            "https://tabs.ultimate-guitar.com/tab/taylor-swift/i-knew-you-were-trouble-chords-1187569")

    expander = ciao2.beta_expander("Tha Supreme")
    if expander.button("No 14"):
        expander.write("https://tabs.ultimate-guitar.com/tab/tha-supreme/no14-chords-3126932")

    expander = ciao2.beta_expander("The Lumineers")
    if expander.button("Ho Hey"):
        expander.write("https://tabs.ultimate-guitar.com/tab/the-lumineers/ho-hey-chords-1047662")

    expander = ciao2.beta_expander("The runaways")
    if expander.button("Cherry bomb"):
        expander.write("https://tabs.ultimate-guitar.com/tab/the-runaways/cherry-bomb-chords-366491")

    expander = ciao2.beta_expander("Tom Odell")
    if expander.button("Another love"):
        expander.write("https://tabs.ultimate-guitar.com/tab/tom-odell/another-love-chords-1198980")

    expander = ciao2.beta_expander("Travis Scott")
    if expander.button("Goosebumps"):
        expander.write("https://tabs.ultimate-guitar.com/tab/travis-scott/goosebumps-chords-1951495")

    expander = ciao2.beta_expander("Twentyone pilots ")
    if expander.button("Migraine"):
        expander.write("https://tabs.ultimate-guitar.com/tab/twenty-one-pilots/migraine-chords-1453839")

    expander = ciao2.beta_expander("Vance joy")
    if expander.button("Fine and the flood"):
        expander.write("https://tabs.ultimate-guitar.com/tab/vance-joy/fire-and-the-flood-chords-1754348")

elif sidebar_page == "Grafici":

    col1, col2 = st.beta_columns([4, 1])
    with col1:
        st.title("Grafici")
        st.header("Ecco la rappresentazione grafica dei parametri analizzati.")
    with col2:
        st.image('https://cdn.dribbble.com/users/5311927/screenshots/11643291/media/9329dee71837445df2ce7f53038309e1.gif', width=180)

    df = pd.read_csv('10k_random_tracks.csv')
#   st.dataframe(data=df)
    df = df.iloc[:100]

    expander = st.beta_expander("Confronto della popolarita` dei primi 100 brani presi in analisi.")
    expander.bar_chart(df.popularity.iloc[:100])

    expander = st.beta_expander("Confronto della durata in millisecondi dei primi 100 brani presi in analisi.")
    expander.bar_chart(df.duration_ms.iloc[:100])

    expander = st.beta_expander("Danzabilità ed energia di ogni canzone")
    expander.bar_chart(df[["danceability", "energy"]].iloc[:100])

    df = pd.read_csv('10k_random_tracks.csv')
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_year"] = df["release_date"].dt.year
    danceability_per_anno = df.groupby("release_year").danceability.mean()

    expander = st.beta_expander("Confronto della danzabilita` negli anni dei primi 100 brani presi in analisi.")
    expander.line_chart(danceability_per_anno)

    st.header("Qua puoi visualizzare grafici radar specifici delle cartteristiche delle canzoni in elenco.")
    option = st.selectbox("Scegli la canzone che vuoi analizzare:", df.name.values)
    st.write("Dati di " + option)
    riga = df[df.name == option].iloc[0]
    st.write(df[df.name == option])
    colonne = [ "danceability", "energy", "loudness", "instrumentalness", "acousticness", "liveness", "speechiness",]
    data_plot = df[df.name == option][colonne]
    data_radar = list(data_plot.iloc[0].values)

    df_plot = pd.DataFrame(dict(
        r=data_radar,
        theta=colonne
    ))
    col1, col2 = st.beta_columns([1, 1])
    with col1:
        fig = px.line_polar(df_plot, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            width=350,  # ho aggiunto width e height
            height=350,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=False
        )
        col1.plotly_chart(fig)
        col1.write("Grafico della canzone scelta.")

    with col2:
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        rigaa = df[df.name == option].iloc[0]
        colonnee = ["acousticness"]
        data_for_istogramma = df[df["name"] == option][colonne]
        data_istogramma = list(data_for_istogramma.iloc[0].values)
        col2.bar_chart(df[["acousticness"]].iloc[:100])
        col2.write("Grafico riferito alle prime 100 canzoni prese in analisi.")

elif sidebar_page == "Bio artisti":
    st.markdown(
        """ 
        <style> 
        .reportview-container { 
            background: url("https://wallpapercave.com/wp/wp3284839.gif") 
        } 
       .sidebar .sidebar-content { 
            background: url("url_goes_here") 
        } 
        </style> 
        """,
        unsafe_allow_html=True
    )
    colonna1, colonna2 = st.beta_columns((5, 2))
    # Modo facile di scrivere testo su streamlit

    colonna1.title("Bio artisti")
    colonna1.header("Conosci ogni singolo dettaglio sulla vita degli artisti!")
    colonna2.write("Seleziona il tuo cantante preferito tra la Gallery")
    df = pd.read_csv("10k_random_tracks.csv")
    artists = list(df["artists"])
    option = colonna2.selectbox("Cerca qui", artists)
    artist = option[0]
    nomecognome = option.split("'")[1]
    # nomecognome2 = nomecognome.split(" ")[0]+"+"+nomecognome.split(" ")[1]
    nomecognomelista = []
    for i in nomecognome.split(" "):
        nomecognomelista.append(i)
    nomecognome4 = ""
    for n in range(len(nomecognomelista)):
        if not n == len(nomecognomelista) - 1:
            nomecognome4 += nomecognomelista[n] + "+"
        else:
            nomecognome4 += nomecognomelista[n]
    colonna1.write(wikipedia.summary(nomecognome4))
    listanomi = wikipedia.search(nomecognome4)

    for nome in listanomi[1:]:
        try:
            flag = False
            if wikipedia.page(nome):
                wikipage = wikipedia.page(nome)
                if wikipage.images:
                    for image in wikipage.images:
                        if "jpg" in image or "png" in image:
                            colonna2.image(image)
                            flag = True
                            # st.write(wikipage.images)
                            # st.image(wikipage.images[0])
                            break
            if flag:
                break
        except ValueError as e:
            st.write(e)

elif sidebar_page == "Tendenze del mondo":
    st.title("Tendenze del mondo")
    st.header("Scopri quali sono le canzoni e gli artisti più seguiti negli anni")

    df_artists = pd.read_csv("top_artists_by_country.csv", index_col=0)
    df_tracks = pd.read_csv("top_tracks_by_country.csv", index_col=0)

    gdf = gpd.read_file("World_Countries__Generalized_.dbf").set_index("ISO").sort_index()

    for i in range(10):
        gdf["artist_" + str(i)] = None
        gdf["track_" + str(i)] = None

    for country, country_df in df_artists.groupby("country"):
        country_artists_ranking = df_artists[df_artists.country == country][["artist_name"]]
        for i in range(len(country_artists_ranking)):
            if country in gdf.index.values:
                try:
                    gdf.loc[country, "artist_" + str(i)] = country_artists_ranking.values[i]
                except:
                    print("gdf", gdf.loc[country, "artist_" + str(i)])
                    print("current_artist", country_artists_ranking.values[i])

    for country, country_df in df_tracks.groupby("country"):
        country_tracks_ranking = df_tracks[df_tracks.country == country][["track_name"]]
        for i in range(len(country_tracks_ranking)):
            if country in gdf.index.values:
                print("gdf", gdf.loc[country, "track_" + str(i)])
                print("currenttrack_", country_tracks_ranking.values[i])
                try:
                    gdf.loc[country, "track_" + str(i)] = country_tracks_ranking.values[i]
                except:
                    print("gdf", gdf.loc[country, "track_" + str(i)])
                    print("currenttrack_", country_tracks_ranking.values[i])

    p = gdf.plot(facecolor= "lightgreen", edgecolor="teal")
    gdf = gdf.dropna()

    hover_data1 = [f"artist_{i}" for i in range(10)]
    hover_data2 = [f"track_{i}" for i in range(10)]

    st.subheader("Mappa interattiva")
    st.write("Puoi anche ingrandire la figura con le ultime freccette a destra")
    fig = px.choropleth(gdf,
                        geojson=gdf.geometry,
                        locations=gdf.index,
                        projection="mercator",
                        hover_data=hover_data1+hover_data2,
                        )
    fig.update_layout(
        height=800,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Guarda le classifiche di una nazione")
    #Selectbox
    option = st.selectbox("Scegli la nazione", df_artists.country.unique())
    st.header("Artisti")
    st.dataframe(df_artists[df_artists.country == option][["artist_name"]])
    st.header("Canzoni")
    st.dataframe(df_tracks[df_tracks.country == option][["track_name", "album_name", "artist_name", "track_share_url"]])
    expander = st.beta_expander("scopri di più")
    expander.dataframe(df_tracks[df_tracks.country == option][
                           ["track_name", "instrumental", "explicit", "has_lyrics", "num_favourite", "track_rating"]])

elif sidebar_page == "Il nostro Team":

    colonna1, colonna2 = st.beta_columns((4, 2))

    # Modo facile di scrivere testo su streamlit
    colonna1.title("MODESTEM")

    colonna1.image("photo5976749182444222219.jpeg")
    colonna1.write("""
        Irene Birolo, Beatrice Berra, Cristina Russo, Mia Marchese, Ilaria Vione, 
        Silvia Cresto, Alissa Rizzo, Emily Glanville, Alice Mocellin, Carola Santoro
    """)

    colonna1.write("Selezionando nel box qui sotto potrai trovare maggiori informazioni su di noi!")

    clicca_qui = colonna1.selectbox(
        "Clicca qui",
        ["Chi siamo?", "Il nostro progetto", "Come abbiamo lavorato?", "Chi ci ha aiutato?",
         "Cosa abbiamo imparato?"]
    )
    if clicca_qui == "Chi siamo?":
        colonna1.write("Siamo un gruppo di dieci ragazze che si sono cimentate nella programmazione in Python e \
                  hanno creato questo sito. Veniamo da licei differenti: dal linguistico, dal classico, dallo \
                  scientifico e da scienze umane. Ci siamo trovate tutte a lavorare al di fuori delle nostre \
                  competenze, aiutandoci a vicenda. \n"
                  "\rL'opportunità di partecipare a questo campus ci è stata offerta dal progetto Stem-Days, per il \
                  quale sono state selezionate ragazze di Torino e dintorni a cui è stato proposto uno stage \
                  interattivo di informatica. Al seguito di due giorni di formazione siamo nate proprio noi, \
                  le MODESTEM! Il nostro nome è facilmente intuibile: è l'unione della parola MODESTE, una nostra \
                  non-qualità e dell'acronimo STEM, utilizzato per indicare le discipline scientifico-tecnologiche.\n"
                  "\rDire che quello che abbiamo fatto è stato semplice non è affatto vero! Con poche conoscenze \
                  informatiche e con compagne appena conosciute, ci siamo ritrovate a creare un sito web dal nulla. \
                  Questo è stato possibile grazie all'aiuto del personale, che in questi giorni ci ha seguito da \
                  vicino, e della fondazione Human+ che ha proposto e realizzato questo progetto."
                 )
    if clicca_qui == "Il nostro progetto":
        colonna1.write("StemDays è un progetto nato dal desiderio di aiutare le ragazze a dimostrare che lo stereotipo \
                 secondo cui le donne non sono portate per la tecnologia è falso.\n"
                 "\rCome dice il nostro tutor Domenico, questo tema è molto importante, in particolare ora, poichè con \
                 la pandemia si sono fatti tanti passi indietro sulle opportunità lavorative delle donne, che in molti \
                 casi hanno vissuto maggior conflitto lavoro-famiglia, secondo una ricerca del Conferenza Nazionale \
                 degli Organismi di Parità il 10% in più di donne rispetto agli uomini si sono trovate a dover \
                 affrontare la difficoltà di conciliare lavoro e famiglia. \
                 Questo progetto si impone l'obiettivo di aumentare il nostro empowerment, dal momento che \
                 c’è bisogno di formazione per le donne perchè, come sapete, ci sono tanti stereotipi e difficoltà ad \
                 accedere al mondo della scienza in generale.\n"
                 "\r L'idea di organizzare questo campus è nata un anno fa quando Patrizia Ghiazza, la presidentessa \
                 della fondazione Human+, ispirandosi al Pink Camp, ha fatto tanta ricerca, ha parlato con tanti \
                 esperti e ha organizzato, con l’aiuto di collaboratori, questa bellissima attività.\n"
                 "\r Quando è arrivato il momento di scegliere le ragazze da coinvolgere, si è deciso che il progetto \n"
                 "non sarebbe stato dedicato solo a coloro che già avevano buone conoscenze informatiche o che avevano \
                 un buon rendimento scolastico, ma la variabile determinante nella scelta sarebbe stata la motivazione,\
                 così da offrire a tutte l'opportunità di partecipare.\n"
                 "\r Inoltre, anche il luogo in cui si è svolta l'attività è tuttal'altro che casuale: il Cottino \
                 Social Impact Campus ha, infatti, una forte attenzione al futuro. Lo dimostra anche il fatto che è \
                 stato costruito nel rispetto dell'ambiente. Quale luogo più adatto per costruire un futuro migliore?\n"
                 "\rAnche la posizione dell'edificio è significativa. Infatti, si trova accanto al Politecnico, ma non \
                 dentro, per sottolineare che questo progetto ha come primo obiettivo quello di aiutarci a crescere \
                 avendo un assaggio del mondo del lavoro e come secondo obiettivo di avvicinarci alle tecnologie."
                 )
    if clicca_qui == "Come abbiamo lavorato?":
        colonna1.write("Durante questi dieci giorni, ci sono state offerte diverse tipologie di attività. Inizialmente \
                  abbiamo lavorato molto su noi stessi e sul team building, per comprendere i nostri difetti e pregi \
                  in modo tale da formare un gruppo consolidato. Dopo giochi teatrali, discorsi e costruzioni manuali \
                  abbiamo invece frequentato diverse lezioni per apprendere teoricamente tutte le basi dell’informatica \
                  e in cosa consiste per davvero la progettazione, in modo tale da informare anche quelle di noi che \
                  ne sapevano meno di informatica. Grazie all’aiuto dei tutors Alessandro, Dena e Giulia, siamo \
                  riusciti a realizzare il sito da noi ideato."
                 )
    if clicca_qui == "Chi ci ha aiutato?":
        colonna1.write("Nella realizzazione di questo progetto siamo state aiutate da molte persone.\n"
                 "\r Cristina e Alberto ci hanno aiutato a socializzare e a diventare un gruppo più unito;\n"
                 "\r Claudio, Alessandro ed Emiliano ci hanno insegnato le basi della tecnologia; \n"
                 "\r Alessandro, Dena e Giulia ci hanno insegnato a programmare in python (nel limite del possibile \
                 visto il tempo) e hanno avuto un ruolo importantissimo, anzi indispensabile, per la creazione di \
                 questa pagina Web;\n"
                 "\r Filippo e Azzurra, invece, ci hanno aiutato a presentare il progetto; \n"
                 "\r Domenico e Fabiola ci hanno seguito durante tutto il percorso offrendoci aiuto e supporto."
                 )
    if clicca_qui == "Cosa abbiamo imparato?":
        colonna1.write("In queste due settimane abbiamo imparato tantissime cose sia in ambito tecnologico che a livello \
                 umano:\n"
                 "\r In ambito tecnologico abbiamo familiarizzato con il computer, chi già non le conosceva ha imparato\
                  le basi dell'informatica e della programmazione e ci siamo cimentate nella programmazione in Python \
                  imparando, chi con più chi con meno difficoltà, a svolgere alcune funzionalità.\n"
                 "\r A livello umano, invece, abbiamo imparato a collaborare, fidandoci l'una dell'altra e \
                 supportandoci a vicenda, soprattutto nella fase opertiva, in il lavoro di una sola non sarebbe\
                 bastato.\n"
                 "\r La presenza di una scadenza di tre giorni ci ha costretto a organizzarci bene.\n"
                 "\r Ci hanno insegnato che l'apprendimento può essere divertente, anche se difficile.\n "
                 "\r Abbiamo trovato molto interessante la scelta di farci dare dei feedback alla fine \
                 di ogni giornata: le formazioni che arricchiscono sono anche quelle in cui vengono ascoltati i feedback per \
                 migliorare; dove l'obbiettivo non è valutarci, ma costruire una relazione con noi."
)
