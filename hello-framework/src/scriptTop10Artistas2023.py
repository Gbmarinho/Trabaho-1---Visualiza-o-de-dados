import pandas as pd

df = pd.read_csv('./data/spotify-2023.csv', encoding='latin1')
df_2023 = df[df['released_year'] == 2023]
artist_streams_2023 = df_2023.groupby('artist(s)_name')['streams'].sum()
top_10_artists_2023 = artist_streams_2023.sort_values(ascending=False).head(10)
top_10_artists_df_2023 = pd.DataFrame({'artist(s)_name': top_10_artists_2023.index, 'streams': top_10_artists_2023.values})
print(top_10_artists_df_2023)
top_10_artists_df_2023.to_csv('./data/top_10_artists_2023.csv', index=False)
