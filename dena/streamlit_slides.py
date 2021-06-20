

#Importare la libreria Python per streamlit
import streamlit as st

#Titolo della pagina
st.title('La mia prima pagina web!')

st.write("Benvenuti nella mia pagina web. L'ho creata con Streamlit!")

# Display image
from PIL import Image

image = Image.open("Dolomites-Italian-Alps.jpg")
st.image(image, caption="Dolomiti!")




# Create and display a dataframe
import pandas as pd

df = pd.DataFrame({
    'column 1': [1, 2, 3, 4],
    'column 2': [4, 3, 2, 1]
})

st.write(df)

st.line_chart(df)






#Leggere file .csv e mettere in un dataframe df_tracks
df_tracks = pd.read_csv("../alecioc/data/10k_random_tracks.csv")
st.write(df_tracks.head(10))

#Fare una nuova colonna "release year" prendendo solo l'anno di release date
df_tracks["release_date"] = pd.to_datetime(df_tracks["release_date"])
df_tracks["release_year"] = df_tracks["release_date"].dt.year

#Ragruppare per anno e prendere la media della colonna danceability
danceability_per_year = df_tracks.groupby("release_year")["danceability"].mean()

#Plottare la media di danceability per anno
st.line_chart(danceability_per_year)