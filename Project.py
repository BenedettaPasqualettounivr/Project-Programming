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

st.text("We starting from an analysis of our dataset in order to understand the data, with code like:")
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
st.text("So we can check the number of songs from these years present in the dataset and,")
st.text("thorough the code")
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
spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)

st.subheader("Then we start to analyse some interesting variables:")
st.text("ARTIST")
st.text("First of all we check how many songs each artist did:")
st.code('''artist=df['artist'].value_counts()''')
artist = spotify_df['artist']
print(artist)
st.text("Then we plot it, in order to see which are the five most important artists:")
st.text("So, the most popular artist is Rihanna, since")
st.code('''pop_artist = df.groupby('artist')[['artist','popularity']].sum().sort_values('popularity',ascending=False).head(10)
print('The most popular artist is', pop_artist.index[0])''')
tp_artists_songs= artist[:5]
tp_artists_name =artist[:5]
fig = plt.figure(figsize = (10, 5))
plt.bar(tp_artists_name,tp_artists_songs,width = 0.4,color="forestgreen")
plt.xlabel("Artists")
plt.ylabel("No of Songs")
plt.title('Top Artists with Hit Songs',color = 'black',fontsize = 20)
plt.show(tp_artists_name, tp_artists_songs)
st.bar_chart(tp_artists_songs, tp_artists_name)

st.text("DURATION")
st.text("Since we want to check the average Duration of Top Hit Songs for each year, we start")
st.text("from the conversion the duration of songs from milliseconds to minutes and seconds.")
st.text("Then we find out the five longest songs")
st.code('''songs_by_duration = df.sort_values("min:sec", ascending=False)[["song", "artist", "min:sec"]]
songs_by_duration[:5]''')
st.text("And the five shortest songs")
st.code('''songs_by_duration[-5:]''')
st.text("Then we analyse the trend during the year of the duration of songs.")
st.text("As we can see here, the duration has a decreasing trend.")
def time_convert(ms):
    sec=ms/1000
    return f"{int(sec//60)}:{int(sec%60)}"
durations = df[['duration_ms','year']].groupby('year').mean().reset_index().iloc[0:20]
durations['min:sec'] = durations['duration_ms'].apply(time_convert)
durations
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

st.text("Then we search the number of songs per year, as we can see here there")
st.text("isn't a specific trend")

