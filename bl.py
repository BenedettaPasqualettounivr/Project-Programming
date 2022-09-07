import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from kmodes.kmodes import KModes
import seaborn as sns
from sklearn.cluster import KMeans
import streamlit as st

spotify_df = pd.read_csv('songs_normalize.csv')
st.title("TOP HITS SPOTIFY FROM 2000 TO 2019")
st.image("logo.png")
st.text("We started from an analysis of our dataset in order to understand the data, with") 
st.text("code like:")
st.text("We started from an analysis of our dataset in order to understand the data, with code like:")
st.code('''spotify_df.shape''')
spotify_df.shape
st.code('''spotify_df.columns''')
spotify_df.columns
st.code ('''spotify_df.info()''')
spotify_df.info()
st.code('''spotify_df.dtypes()''')
st.code('''spotify_df.head(5)''')
spotify_df.head(5)
st.code('''spotify_df.tail(5)''')
spotify_df.tail(5)
st.code('''spotify_df.describe()''')
spotify_df.describe()

st.text("Next, we proceed to clean our data")
st.text("First of all we want to see the sum of null cells")
st.code('''spotify_df.isnull().sum()''')
spotify_df.isnull().sum()
st.text("Then we check the release year present in the dataset")
st.code('''spotify_df.year.unique()''')
spotify_df.year.unique()
st.text("We can see that there are some songs that are published outside the interval") 
st.text("2000-2019.") 
st.text("So we can check the number of songs from these years present in the dataset ")
st.text("thorough the code:")
st.code('''s1=(len(spotify_df.query('year==1998')))
s2=(len(spotify_df.query('year==1999')))
s3=(len(spotify_df.query('year==2020')))
s= s1+s2+s3''')
s1=(len(spotify_df.query('year==1998')))
s2=(len(spotify_df.query('year==1999')))
s3=(len(spotify_df.query('year==2020')))
s= s1+s2+s3
print("The total number of songs:",s)
st.text("We can see that the songs the are outside the interval are 42.")
st.text("Thus there are 42 songs from all 3 years combined. The goal of the dataset is to")
st.text("analyse data from the timeperiod [2000-2019] and hence any other data outside this") 
st.text("timeline can be neglected.")
st.text("Hence we would be removing all the data pertaining to these years from the dataframe,") 
st.text("creating a new dataset")
st.code('''spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)''')
spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)

st.subheader("Then we start to analyse some interesting variables:")
st.subheader("ARTIST")
st.text("First of all we check how many songs each artist did:")
st.code('''artist=df['artist'].value_counts()''')
artist=df['artist'].value_counts()
tp_artists_songs= artist[:5]
tp_artists_name =artist[:5].index
fig1 = plt.figure(figsize = (10, 5))
plt.bar(tp_artists_name,tp_artists_songs,width = 0.4,color="forestgreen")
plt.xlabel("Artists")
plt.ylabel("No of Songs")
plt.title('Top Artists with Hit Songs',color = 'black',fontsize = 20)
plt.show()
st.pyplot(fig1)
st.text("Then we plot it, in order to see which are the five most important artists:")
st.text("So, the most popular artist is Rihanna,")
st.code('''pop_artist = df.groupby('artist')[['artist','popularity']].sum().sort_values('popularity',ascending=False).head(10)
print('The most popular artist is', pop_artist.index[0])''')
pop_artist = df.groupby('artist')[['artist','popularity']].sum().sort_values('popularity',ascending=False).head(10)
print('The most popular artist is', pop_artist.index[0])

st.subheader("GENRE")
st.text("Now we analize the variable Genre. We count how many songs there are for each genre.")
st.code('''genre = spotify_df['genre'].value_counts()''')
genre = df['genre'].value_counts()
st.text("In order to better visualize this we made this barchart.")
fig2 = plt.figure(figsize=(15,10))
sns.countplot(y='genre', data=df,palette="rocket")
plt.show()
st.pyplot(fig2)
st.text("Here we can see that the most populated genre is pop.")
st.text("There are a lot of genres so we decide to focus on the first 10 most popular.")
st.code('''genre_distribution = pd.DataFrame(spotify_df.genre.value_counts().rename_axis('Genre').reset_index(
  name='total'))
genre_distribution.head(10)''')
genre_distribution = pd.DataFrame(spotify_df.genre.value_counts().rename_axis('Genre').reset_index(
    name='total'))
genre_distribution.head(10)
st.text("So we made a pie chart to see their distribution in percentage.")
fig3 = plt.figure(figsize=(8,2))
fig = px.pie(genre_distribution.head(10), names = 'Genre',
      values = 'total', template = 'seaborn', title = 'Top 10 genres distribution')
fig.update_traces(rotation=90, pull = [0.2,0.06,0.06,0.06,0.06], textinfo = "percent+label")
fig.show()
st.pyplot(fig3)

st.text("Focusing then on the Hits, we can now see the Top 5 Genres which are hits.")
tp_genres=genre[:5]
tp_genres_names=genre[:5].index
fig4 = plt.figure(figsize = (10, 5))
plt.bar(tp_genres_names,tp_genres,width = 0.4,color='b')
plt.xlabel("Genres")
plt.ylabel("No of songs")
plt.title('Top 5 Genres or Combination of Genres which are hits',color = 'black',fontsize = 20)
plt.show()
st.pyplot(fig4)
print('The most popular genre is', genre.index[0])
st.text("So, the most popular genre is pop.")

st.subheader("DURATION")
st.text("Since we want to check the average duration of Top Hit Songs for each year, we start")
st.text("from the conversion of the duration of songs from milliseconds to minutes and seconds.")
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

x=df["year"].unique()
x=sorted(x)
y=(durations["min:sec"])
x=pd.Series(x)
st.text("Then we analyse the trend during the year of the duration of songs.")
fig5 = plt.figure(figsize=(12,8))
sns.lineplot(x,y,data=df)
plt.title('Change in the Duration of Song',fontsize=15)
plt.xlabel('Years',size=10)
plt.ylabel('Time',size=10)
plt.show()
st.pyplot(fig5)
st.text("As we can see here, the duration has a decreasing trend.")
st.text("Then we find out the five longest songs")
st.code('''songs_by_duration = df.sort_values("min:sec", ascending=False)[["song", "artist", "min:sec"]])
songs_by_duration[:5]''')
songs_by_duration[:5]
st.text("And the five shortest songs")
st.code('''songs_by_duration[-5:]''')
songs_by_duration[-5:]

st.subheader("EXPLICIT CONTENT")
st.text("Now we want to have a view of the amount of explicit content in the top-hits.")
st.text("We firstly count the amount of explicit and not-explicit content and then we plot it with a Barchart")
st.text("and with a piechart.")
st.code('''data=spotify_df['explicit'].value_counts()
explicit_songs_or_not = (spotify_df.explicit.value_counts().rename_axis('Explicit').reset_index(name = 'songs'))''')
explicit_songs_or_not = (spotify_df.explicit.value_counts().rename_axis('Explicit').reset_index(name = 'songs'))

data=df['explicit'].value_counts()
fig6 = plt.figure(figsize=(10,8))
plt.title("Total Amount of Explicit Songs",fontsize=14)
plt.ylabel("No of Songs")
plt.xlabel("Explicitness")
data.plot(kind='bar',color=['lightblue', 'violet'])
plt.show()
st.pyplot(fig6)

st.text("Here we used the piechart in order to have the percentage")

fig7 = plt.figure(figsize=(12,8))
fig = px.pie(explicit_songs_or_not, names = ['Not explicit','Explicit'], 
             values = 'songs', template='seaborn',
            title = 'Percentage of explicit content in the top hits from 2000 to 2019')
fig.show()
st.pyplot(fig7)

st.text("Now, we visualize the number of top-hits wich are explicit over the years. ")
st.code('''song_yr_explicit = spotify_df.groupby(['year','explicit']).size().unstack(fill_value=0).reset_index()
song_yr_explicit.rename(columns={False:'Clean', True: 'Explicit'}, inplace=True)''')
print ('Explicit Is True =',(spotify_df[spotify_df['explicit']==True]['popularity']).count())
print ('Explicit Is False =',(spotify_df[spotify_df['explicit']==False]['popularity']).count())
st.text("Here we can see another way to visualize the amount of explicit and non explicit content by a different")
st.text("barchart.")
fig8 = plt.figure(figsize=(12,6))
df[df['explicit']==True]['popularity'].hist(bins=30, color='blue',alpha=0.5,
                                                        label='Explicit Is True')
df[df['explicit']==False]['popularity'].hist(bins=30, color='green',alpha=0.5,
                                                        label='Explicit Is False')

plt.legend()
st.pyplot(fig8)

st.subheader("DANCEABILITY")
st.text("Another interesting varibale is deanceability, as we can see by this graph:")
st.text("There is a correlation between Danceability and density.")
plt.title("Danceability of top-hits over the years:",size=15)
fig9 = plt.figure(figsize=(10,10))
sns.distplot(df['danceability'],color="r")
plt.show()
st.pyplot(fig9)
print("Average danceability of top-hits:\n",df['danceability'].mean())
print("Maximum danceability of top-hits:\n")
df.loc[df['danceability']==df['danceability'].max()]

st.subheader("CORRELATION")
st.text("Now we will analyze the correlation between various features. To do this we create a mew dataframe to find")
st.text("the relation among the numerical variables present in the dataset. ")
st.code('''df_new = spotify_df[['duration_ms', 'year', 'popularity', 'danceability', 'energy', 
     'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]''')
st.text("The result of the study is the following heatmap where we plot all the correlations between the variables.")
df_new = df[['duration_ms', 'year', 'popularity', 'danceability', 'energy', 
     'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
fig10 = plt.figure(figsize=(15,8))
sns.heatmap(df_new.corr(), annot = True, linewidths = .5, fmt = '.2f',cmap = "YlGn")
plt.title('Correlation among measures', size = 25)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12, rotation = 50)
plt.show()
st.pyplot(fig10)

st.subheader("FOCUS ON RIHANNA")
st.text("Since the most popular artist is Rihanna, we decide to do a focus on her.")
st.text("We filter the dataset in order to obtain only the songs of Rihanna.")
st.code("rihanna_df = spotify_df[spotify_df['artist'] == 'Rihanna']")
rihanna_df = df[df['artist'] == 'Rihanna']
st.text("We count then the number of songs she has, which is 23.")
st.code('''len(rihanna_df.song.unique())''')
len(rihanna_df.song.unique())
st.text("We now use a code to get the popularity and the number of songs per year.")

fig11 = plt.figure(figsize=(8,2))
fig = px.bar(rihanna_df, x='year', y='popularity',title = 'Total Popularity of song by year')
fig.show()
st.pyplot(fig11)

st.text("Then in order to have an overview of Rihanna we calculate the sum of her")
st.text("popularity:")

fig12 = plt.figure(figsize=(8,3))
fig = px.histogram(rihanna_df, x="year", y="popularity",
                   hover_data=rihanna_df.columns)
fig.show()
st.pyplot(fig12)

st.text("Then we proceed calculating her five best songs:")
rihanna_df = rihanna_df.sort_values('popularity',ascending=False)
rihanna_df[['song','year','popularity','genre']].head()

fig13 = plt.figure(figsize=(15,10))
sns.heatmap(rihanna_df.corr())
st.pyplot(fig13)


cost = []
K = range(1,20)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init = 'random', n_init = 5, verbose=1)
    kmode.fit_predict(df)
    cost.append(kmode.cost_)
    
st.subheader("CLUSTERING")
st.text("Now, we use clustering in order to understand how data are grouped")
st.text("First of all, we use the Elbow method to see which is the best number of clusters:")
fig14 = plt.figure(figsize=(15,10))
plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Cost')
plt.title('Elbow Method For Optimal k')
plt.show()
st.pyplot(fig14)

kmode = KModes(n_clusters=5, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(df)
df.insert(0, 'Cluster', clusters, True)

st.text("Then, we plot the variables energy and loudness to see the distribution:")
fig15 = plt.figure(figsize=(20,16))
plt.scatter(df['energy'], df['loudness'])
plt.xlabel('Energy')
plt.ylabel('Loudness')
st.pyplot(fig15)
st.text("Through some codes like:")
st.code('''square_distances = []
x = df[['energy','loudness']]
for i in range(1, 11):
    km = KMeans(n_clusters=5, random_state=42)
    km.fit(x)
    square_distances.append(km.inertia_)
km = KMeans(n_clusters=5, random_state=42)
y_pred = km.fit_predict(x)''')
square_distances = []
x = df[['energy','loudness']]
for i in range(1, 11):
    km = KMeans(n_clusters=5, random_state=42)
    km.fit(x)
    square_distances.append(km.inertia_)
km = KMeans(n_clusters=5, random_state=42)
y_pred = km.fit_predict(x)
st.text("We find out that the clusters are")
fig16 = plt.figure(figsize=(20,30))
labels = ['pop', 'rock', 'R&B', 'deance', 'hip-hop']
for i in range(5):
    plt.scatter(x.loc[y_pred==i, 'energy'], x.loc[y_pred==i, 'loudness'], label=labels[i])

plt.xlabel('Energy')
plt.ylabel('Loudness')
plt.legend()
plt.show()
st.pyplot(fig16)