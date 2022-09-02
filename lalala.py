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

st.text("We starting from an analysis of our dataset in order to understand our data, with code like:")
st.code('''spotify_df.shape''')
st.code ('''spotify_df.info()''')
st.code('''spotify_df.dtypes''')
st.code('''spotify_df.head(5)''')
st.code('''spotify_df.describe()''')

st.text("Next, we proceed to clean our data:")
st.text("To see the sum of null cells")
st.code('''spotify_df.isnull().sum()''')
st.text("Checking the year of release present in the dataset")
st.code('''spotify_df.year.unique()''')
st.text("We can see that there are some songs that are published outside the interval 2000-2019. So we can check the number of songs from these years present in the dataset")
st.text("and, thorough the code")
st.code('''s1=(len(spotify_df.query('year==1998')))
s2=(len(spotify_df.query('year==1999')))
s3=(len(spotify_df.query('year==2020')))
s= s1+s2+s3''')
st.text("We can see that the songs the are outside the interval are 42")
st.text("Thus there are 42 songs from all 3 years combined. The goal of the dataset is to analyse data from the timeperiod [2000-2019] and hence any other data outside this timeline can be neglected")
st.text("Hence we would be removing all the data pertaining to these years from the dataframe, creating a new dataset")
st.code('''spotify_df_years_drop = spotify_df[(spotify_df['year'] <2000) | (spotify_df['year'] > 2019)].index
df = spotify_df.drop(spotify_df_years_drop)''')

st.subheader("Then we start to analyse some interesting variables:")
st.text("ARTIST")
st.text("First of all we check how many songs each artist did:")
st.code('''artist=df['artist'].value_counts()''')
st.text("Then we plot it, in order to see which are the five most important artists:")
st.bar_chart(data="artist")