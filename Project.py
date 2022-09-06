import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

spotify_df = ("songs_normalize.csv")

st.title("TOP HITS SPOTIFY FROM 2000 TO 2019")
st.image("logo.png")

st.text("We started from an analysis of our dataset in order to understand the data, with") 
st.text("code like:")
st.code('''spotify_df.shape''')
st.code('''spotify_df.columns''')
st.code ('''spotify_df.info()''')
st.code('''spotify_df.dtypes''')
st.code('''spotify_df.head(5)''')
st.code('''spotify_df.tail(5)''')
st.code('''spotify_df.describe()''')

st.text("Next, we proceed to clean our data")
st.text("First of all we want to see the sum of null cells")
st.code('''spotify_df.isnull().sum()''')
st.text("Then we check the release year present in the dataset")
st.code('''spotify_df.year.unique()''')
st.text("We can see that there are some songs that are published outside the interval") 
st.text("2000-2019.") 
st.text("So we can check the number of songs from these years present in the dataset ")
st.text("thorough the code:")
st.code('''s1=(len(spotify_df.query('year==1998')))
s2=(len(spotify_df.query('year==1999')))
s3=(len(spotify_df.query('year==2020')))
s= s1+s2+s3''')
st.text("We can see that the songs the are outside the interval are 42.")
st.text("Thus there are 42 songs from all 3 years combined. The goal of the dataset is to")
st.text("analyse data from the timeperiod [2000-2019] and hence any other data outside this") 
st.text("timeline can be neglected.")
st.text("Hence we would be removing all the data pertaining to these years from the dataframe,") 
st.text("creating a new dataset")
st.code('''spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)''')

st.subheader("Then we start to analyse some interesting variables:")
st.text("ARTIST")
st.text("First of all we check how many songs each artist did:")
st.code('''artist=df['artist'].value_counts()''')
st.text("Then we plot it, in order to see which are the five most important artists:")
st.text("So, the most popular artist is Rihanna, since")
st.code('''pop_artist = df.groupby('artist')[['artist','popularity']].sum().sort_values('popularity',ascending=False).head(10)
print('The most popular artist is', pop_artist.index[0])''')

st.subheader("GENRE")
st.text("Now we analize the variable Genre. We count how many songs there are for each genre.")
st.code('''genre = spotify_df['genre'].value_counts()''')
st.text("In order to better visualize this we made this barchart.")
plt.figure(figsize=(15,10))
sns.countplot(y='genre', data=spotify_df,palette="rocket")
plt.show()

st.text("Here we can see that the most populated genre is pop.")
st.text("There are a lot of genres so we decide to focus on the first 10 most popular.")
st.code('''genre_distribution = pd.DataFrame(spotify_df.genre.value_counts().rename_axis('Genre').reset_index(
    name='total'))
genre_distribution.head(10)''')
st.text("So we made a pie chart to see their distribution in percentage.")
plt.figure(figsize=(8,2))
fig = px.pie(genre_distribution.head(10), names = 'Genre',
      values = 'total', template = 'seaborn', title = 'Top 10 genres distribution')
fig.update_traces(rotation=90, pull = [0.2,0.06,0.06,0.06,0.06], textinfo = "percent+label")
fig.show()
st.text("Focusing then on the Hits, we can now see the Top 5 Genres which are hits.")
st.code('''tp_genres=genre[:5]
tp_genres_names=genre[:5].index''')

fig = plt.figure(figsize = (10, 5))
plt.bar(tp_genres_names,tp_genres,width = 0.4,color='b')
plt.xlabel("Genres")
plt.ylabel("No of songs")
plt.title('Top 5 Genres or Combination of Genres which are hits',color = 'black',fontsize = 20)
plt.show()
st.text("Pop seems to be the most popular type of genre. In fact, 428 songs of the spotify's")
st.text("top-hits songs since 2000-2019 belong to pop. This is followed by")
st.text("hip-hop,pop which is the 2nd most popular conbination of genre.")

st.subheader("EXPLICIT CONTENT")
st.text("Now we want to have a view of the amount of explicit content in the top-hits.")
st.text("We firstly count the amount of explicit and not-explicit content and then we plot it with a Barchart")
st.text("and with a piechart.")
st.code('''data=spotify_df['explicit'].value_counts()
explicit_songs_or_not = (spotify_df.explicit.value_counts().rename_axis('Explicit').reset_index(name = 'songs'))
explicit_songs_or_not''')
plt.figure(figsize=(10,8))
plt.title("Total Amount of Explicit Songs",fontsize=14)
plt.ylabel("No of Songs")
plt.xlabel("Explicitness")
data.plot(kind='bar',color=['lightblue', 'violet'])
plt.show()
st.text("Here we used the piechart in order to have the percentage")
fig = px.pie(explicit_songs_or_not, names = ['Not explicit','Explicit'], 
             values = 'songs', template='seaborn',
            title = 'Percentage of explicit content in the top hits from 2000 to 2019')
fig.show()
st.text("Now, we visualize the number of top-hits wich are explicit over the years. ")
st.code('''song_yr_explicit = spotify_df.groupby(['year','explicit']).size().unstack(fill_value=0).reset_index()
song_yr_explicit.rename(columns={False:'Clean', True: 'Explicit'}, inplace=True)''')
plt.figure(figsize=(14,8))
plt.title("Top hits each year which are explicit",fontsize=15)
c1 = sns.barplot(x="year",y="Explicit",data=song_yr_explicit,palette="mako")
c1.bar_label(c1.containers[0],size = 15)
plt.show()
st.text("Here we can see another way to visualize the amount of explicit and non explicit content by a different")
st.text("barchart.")
plt.figure(figsize=(12,6))
spotify_df[spotify_df['explicit']==True]['popularity'].hist(bins=30, color='blue',alpha=0.5,
                                                        label='Explicit Is True')
spotify_df[spotify_df['explicit']==False]['popularity'].hist(bins=30, color='green',alpha=0.5,
                                                        label='Explicit Is False')
plt.legend()

st.subheader("CORRELATION")
st.text("Now we will analyze the correlation between various features. To do this we create a mew dataframe to find")
st.text("the relation among the numerical variables present in the dataset. ")
st.code('''df_new = spotify_df[['duration_ms', 'year', 'popularity', 'danceability', 'energy', 
     'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]''')
st.text("The result of the study is the following heatmap where we plot all the correlations between the variables.")
plt.figure(figsize=(15,8))
sns.heatmap(df_new.corr(), annot = True, linewidths = .5, fmt = '.2f',cmap = "YlGn")
plt.title('Correlation among measures', size = 25)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12, rotation = 50)
plt.show()

st.subheader("FOCUS ON RIHANNA")
st.text("Since the most popular artist is Rihanna, we decide to do a focus on her.")
st.text("We filter the dataset in order to obtain only the songs of Rihanna.")
st.code("rihanna_df = spotify_df[spotify_df['artist'] == 'Rihanna']")
st.text("We count then the number of songs she has, which is 23.")
st.code('''len(rihanna_df.song.unique())''')
st.text("We now use a code to get the popularity and the number of songs per year.")
fig = px.bar(rihanna_df, x='year', y='popularity',title = 'Total Popularity of song by year')
fig.show()





