import pandas as pd
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
    ["Home", "Grafici", "Il nostro Team"]
)

if sidebar_page == "Home":

    # Modo facile di scrivere testo su streamlit
    st.title("Webby")
    st.header("Benvenut* in Webby, un progetto per STEM days 2021!")
    st.text("Usa il menu sulla sinistra per navigare fra le possibili schermate.")

    #Expander
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")

    button = st.button("Click me")
    if button:
        st.write("Ho sciacciato")
    else:
        st.write("Non ho sciacciato")


    #Decide placement of an image/text
    columns = st.beta_columns((1, 1, 1, 1))

    from PIL import Image

    image = Image.open("../dena/Dolomites-Italian-Alps.jpg")
    # st.image(image, caption="Dolomiti!")

    columns[3].image(image)

elif sidebar_page == "Grafici":
    df = pd.read_csv("../alecioc/data/10k_random_tracks.csv")
    # st.write(df["name"])
    titles = list(df["name"])

    option = st.selectbox(
        'Which song would you like to see?',
         titles)

    'You selected: ', option

    df[df["name"] == option]

    #Radarplot
    columns_for_radar = ["danceability", "energy", "liveness", "speechiness", "acousticness"]
    data_for_radar = df[df["name"] == option][columns_for_radar]
    data_for_radar_plot = list(data_for_radar.iloc[0].values)

    import plotly.express as px
    import pandas as pd

    df = pd.DataFrame(dict(
        r = data_for_radar_plot,
        theta=columns_for_radar
    ))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=False
    )
    st.plotly_chart(fig)

    #Barplot
    fig2 = px.bar(x=columns_for_radar, y=data_for_radar_plot, labels=dict(x="Attributo della canzone", y="Quantità"))
    fig2.update_layout(
        showlegend=False,

    )

    st.plotly_chart(fig2)

    columns = st.beta_columns((1, 1,))
    columns[0].plotly_chart(fig)
    columns[1].plotly_chart(fig2)




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





