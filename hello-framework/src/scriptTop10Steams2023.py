import pandas as pd

df = pd.read_csv('./data/spotify-2023.csv', encoding='latin1')
df_2023 = df[df['released_year'] == 2023]
top_10_songs_2023 = df_2023.sort_values(by='streams', ascending=False).head(10)
print(top_10_songs_2023)
top_10_songs_2023.to_csv('./data/top_10_streams_2023.csv', index=False)
