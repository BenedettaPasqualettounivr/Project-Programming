import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from kmodes.kmodes import KModes
import seaborn as sns
from sklearn.cluster import KMeans

spotify_df = pd.read_csv('songs_normalize.csv')
spotify_df.shape
spotify_df.info()
spotify_df.columns
spotify_df.dtypes
spotify_df.head(5)
spotify_df.tail(5)
spotify_df.describe()

spotify_df.isnull().sum()
spotify_df.year.unique()
s1=(len(spotify_df.query('year==1998')))
s2=(len(spotify_df.query('year==1999')))
s3=(len(spotify_df.query('year==2020')))
s= s1+s2+s3
print("The total number of songs:",s)
spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)

artist=df['artist'].value_counts()
tp_artists_songs= artist[:5]
tp_artists_name =artist[:5].index
fig = plt.figure(figsize = (10, 5))
plt.bar(tp_artists_name,tp_artists_songs,width = 0.4,color="forestgreen")
plt.xlabel("Artists")
plt.ylabel("No of Songs")
plt.title('Top Artists with Hit Songs',color = 'black',fontsize = 20)
plt.show()
pop_artist = df.groupby('artist')[['artist','popularity']].sum().sort_values('popularity',ascending=False).head(10)
print('The most popular artist is', pop_artist.index[0])

genre = df['genre'].value_counts()
plt.figure(figsize=(15,10))
sns.countplot(y='genre', data=df,palette="rocket")
plt.show()
genre_distribution = pd.DataFrame(spotify_df.genre.value_counts().rename_axis('Genre').reset_index(
    name='total'))
genre_distribution.head(10)
plt.figure(figsize=(8,2))
fig = px.pie(genre_distribution.head(10), names = 'Genre',
      values = 'total', template = 'seaborn', title = 'Top 10 genres distribution')
fig.update_traces(rotation=90, pull = [0.2,0.06,0.06,0.06,0.06], textinfo = "percent+label")
fig.show()
tp_genres=genre[:5]
tp_genres_names=genre[:5].index
fig = plt.figure(figsize = (10, 5))
plt.bar(tp_genres_names,tp_genres,width = 0.4,color='b')
plt.xlabel("Genres")
plt.ylabel("No of songs")
plt.title('Top 5 Genres or Combination of Genres which are hits',color = 'black',fontsize = 20)
plt.show()
print('The most popular genre is', genre.index[0])

def time_convert(ms):
    sec=ms/1000
    return f"{int(sec//60)}:{int(sec%60)}"
durations = df[['duration_ms','year']].groupby('year').mean().reset_index().iloc[0:20]
durations['min:sec'] = durations['duration_ms'].apply(time_convert)
def ms_to_min_sec(ms):
    sec = ms/1000
    return f"{int(sec//60)}:{int(sec%60)}"

df['min:sec'] = df['duration_ms'].apply(ms_to_min_sec)
songs_by_duration = df.sort_values("min:sec", ascending=False)[["song", "artist", "min:sec"]]
songs_by_duration[:5]
songs_by_duration[-5:]
x=df["year"].unique()
x=sorted(x)
y=(durations["min:sec"])
x=pd.Series(x)
plt.figure(figsize=(12,8))
sns.lineplot(x,y,data=df)
plt.title('Change in the Duration of Song',fontsize=15)
plt.xlabel('Years',size=10)
plt.ylabel('Time',size=10)
plt.show()
df.groupby("year")["song"].count().plot()

explicit_songs_or_not = (spotify_df.explicit.value_counts().rename_axis('Explicit').reset_index(name = 'songs'))
data=df['explicit'].value_counts()
plt.figure(figsize=(10,8))
plt.title("Total Amount of Explicit Songs",fontsize=14)
plt.ylabel("No of Songs")
plt.xlabel("Explicitness")
data.plot(kind='bar',color=['lightblue', 'violet'])
plt.show()
fig = px.pie(explicit_songs_or_not, names = ['Not explicit','Explicit'], 
             values = 'songs', template='seaborn',
            title = 'Percentage of explicit content in the top hits from 2000 to 2019')
fig.show()
print ('Explicit Is True =',(spotify_df[spotify_df['explicit']==True]['popularity']).count())
print ('Explicit Is False =',(spotify_df[spotify_df['explicit']==False]['popularity']).count())
plt.figure(figsize=(12,6))
df[df['explicit']==True]['popularity'].hist(bins=30, color='blue',alpha=0.5,
                                                        label='Explicit Is True')
df[df['explicit']==False]['popularity'].hist(bins=30, color='green',alpha=0.5,
                                                        label='Explicit Is False')

plt.legend()

plt.figure(figsize=(10,10))
plt.title("Danceability of top-hits over the years:",size=15)
sns.distplot(df['danceability'],color="r")
plt.show()
print("Average danceability of top-hits:\n",df['danceability'].mean())
print("Maximum danceability of top-hits:\n")
df.loc[df['danceability']==df['danceability'].max()]

df_new = df[['duration_ms', 'year', 'popularity', 'danceability', 'energy', 
     'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
plt.figure(figsize=(15,8))
sns.heatmap(df_new.corr(), annot = True, linewidths = .5, fmt = '.2f',cmap = "YlGn")
plt.title('Correlation among measures', size = 25)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12, rotation = 50)
plt.show()

rihanna_df = df[df['artist'] == 'Rihanna']
len(rihanna_df.song.unique())
fig = px.bar(rihanna_df, x='year', y='popularity',title = 'Total Popularity of song by year')
fig.show()
px.histogram(rihanna_df, x="year", y="popularity",
                   hover_data=rihanna_df.columns)
rihanna_df = rihanna_df.sort_values('popularity',ascending=False)
rihanna_df[['song','year','popularity','genre']].head()
plt.figure(figsize=(15,10))
sns.heatmap(rihanna_df.corr())

cost = []
K = range(1,20)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init = 'random', n_init = 5, verbose=1)
    kmode.fit_predict(df)
    cost.append(kmode.cost_)
    
plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Cost')
plt.title('Elbow Method For Optimal k')
plt.show()
kmode = KModes(n_clusters=5, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(df)
df.insert(0, 'Cluster', clusters, True)
plt.figure(figsize=(20,16))
plt.scatter(df['energy'], df['loudness'])
plt.xlabel('Energy')
plt.ylabel('Loudness')
square_distances = []
x = df[['energy','loudness']]
for i in range(1, 11):
    km = KMeans(n_clusters=5, random_state=42)
    km.fit(x)
    square_distances.append(km.inertia_)
km = KMeans(n_clusters=5, random_state=42)
y_pred = km.fit_predict(x)
plt.figure(figsize=(20,30))
labels = ['pop', 'rock', 'R&B', 'deance', 'hip-hop']
for i in range(5):
    plt.scatter(x.loc[y_pred==i, 'energy'], x.loc[y_pred==i, 'loudness'], label=labels[i])

plt.xlabel('Energy')
plt.ylabel('Loudness')
plt.legend()
plt.show()
