import pandas as pd

df = pd.read_csv('./data/spotify-2023.csv', encoding='latin1')
artist_streams = df.groupby('artist(s)_name')['streams'].sum()
top_10_artists = artist_streams.sort_values(ascending=False).head(10)
top_10_artists_df = pd.DataFrame({'artist(s)_name': top_10_artists.index, 'streams': top_10_artists.values})
print(top_10_artists_df)
top_10_artists_df.to_csv('./data/top_10_artists.csv', index=False)

