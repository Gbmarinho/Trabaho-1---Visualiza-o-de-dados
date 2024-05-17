import pandas as pd

df = pd.read_csv('./data/spotify-2023.csv', encoding='latin1')
df_2023 = df[df['released_year'] == 2023]
top_10_apple_charts_2023 = df_2023.sort_values(by='in_shazam_charts', ascending=False).head(10)
top_10_apple_charts_2023 = top_10_apple_charts_2023[['track_name', 'in_shazam_charts', 'streams']]
print(top_10_apple_charts_2023)
top_10_apple_charts_2023.to_csv('./data/top_10_shazam_charts_2023.csv', index=False)
