# dataframe, leggi pezzi di csv

import pandas as pd

df = pd.read_csv("../alecioc/data/10k_random_tracks.csv", index_col=0)

#print(df.index)

print(df.shape)

print(df[["name", "popularity"]])

print(df.iloc[7])

