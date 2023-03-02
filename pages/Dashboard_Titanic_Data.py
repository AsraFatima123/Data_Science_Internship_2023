import streamlit as st
from matplotlib import image
import os
import pandas as pd
import plotly.express as px
import plotly


st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
st.dataframe(df)

Embark_town = st.selectbox("Please select the town", df["embark_town"].unique())


fig1 = px.histogram(df[df['embark_town']==Embark_town], x='sex')
fig1

fig2 = px.histogram(df[df['embark_town']==Embark_town], x='pclass')
fig2