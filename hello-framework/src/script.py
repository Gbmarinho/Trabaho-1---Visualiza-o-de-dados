import pandas as pd

df = pd.read_csv('./data/spotify-2023.csv', encoding='latin1')
print(df.head())
top_10_songs = df.sort_values(by='streams', ascending=False).head(10)
print(top_10_songs)
top_10_songs.to_csv('./data/top_10_streams.csv', index=False)