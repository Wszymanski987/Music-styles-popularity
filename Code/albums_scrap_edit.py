import pandas as pd
df = pd.read_csv('/path/albums_scraping_pagin1-kopia.csv',
                 delimiter=';', dtype=str)

print(df.Style.dtype)

df['Ratings'] = df['Ratings'].fillna(0)
df['Votes '] = df['Votes '].fillna(0)

df = (df[df.Band.str.contains('-', na=False)])
df = (df[~df.Band.str.contains('Post-rock', na=False)])

df['Style'] = df['Style'].fillna(0)
df['Style'] = df['Style'].replace(0, 'unknown')

df[['Band_Name', 'Album']] = df['Band'].str.split(pat='-', n=1, expand=True)

df.drop(columns=['Band'], inplace=True)

df.to_csv('Albums_1_Edited.csv', index=False)

df = pd.read_csv(
    '/path/albums_scraping_pagin2-kopia.csv', delimiter=';', dtype=str)

df['Ratings'] = df['Ratings'].fillna(0)
df['Votes'] = df['Votes'].fillna(0)
df = (df[df.Band.str.contains('-', na=False)])
df = (df[~df.Band.str.contains('Post-rock', na=False)])


df['Style'] = df['Style'].fillna(0)
df['Style'] = df['Style'].replace(0, 'unknown')

df[['Band_Name', 'Album']] = df['Band'].str.split(pat='-', n=1, expand=True)

df.drop(columns=['Band'], inplace=True)
print(df.head)

df.to_csv('Albums_2_Edited.csv', index=False)
