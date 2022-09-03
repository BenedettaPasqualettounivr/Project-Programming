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

st.text("We started from an analysis of our dataset in order to understand the data, with code like:")
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
st.text("BAR CHART")
st.text("Here we can see that the most populated genre is pop.")
st.text("There are a lot of genres so we decide to focus on the first 10 most popular.")
st.code('''genre_distribution = pd.DataFrame(spotify_df.genre.value_counts().rename_axis('Genre').reset_index(
    name='total'))
genre_distribution.head(10)''')
st.text("So we made a pie chart to see their distribution in percentage.")
st.text("Focusing then on the Hits, we can now see the Top 5 Genres which are hits.")
st.code('''tp_genres=genre[:5]
tp_genres_names=genre[:5].index''')
st.text("BAR CHART")
st.text("Pop seems to be the most popular type of genre. In fact, 428 songs of the")
st.text("top-hits spotify songs since 2000-2019 belong to pop. This is followed by")
st.text("hip-hop,pop which is the 2nd most popular conbination of genre.")

st.subheader("EXPLICIT CONTENT")
st.text("Now we want to have a view of the amount of explicit content in the top-hits.")
st.text("We firstly count the amount of explicit and not-explicit content and then we plot it with a Barchart")
st.text("and with a piechart.")
st.code('''data=spotify_df['explicit'].value_counts()
explicit_songs_or_not = (spotify_df.explicit.value_counts().rename_axis('Explicit').reset_index(name = 'songs'))
explicit_songs_or_not''')
st.text("BARCHART")
st.text("Here we used the piechart in order to have the percentage")
st.text("PIECHART")
st.text("Now, we visualize the number of top-hits wich are explicit over the years. ")
st.code('''song_yr_explicit = spotify_df.groupby(['year','explicit']).size().unstack(fill_value=0).reset_index()
song_yr_explicit.rename(columns={False:'Clean', True: 'Explicit'}, inplace=True)''')
st.text("BARCHART")
st.text("Here we can see another way to visualize the amount of explicit and non explicit content by a different")
st.text("barchart.")
st.text(BARCHART)

st.subheader("CORRELATION")






