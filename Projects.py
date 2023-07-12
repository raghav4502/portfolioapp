import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("My Projects")

col3, col4 = st.columns(2)

df = pandas.read_csv("mysite.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])