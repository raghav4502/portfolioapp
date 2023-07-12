import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=350)

with col2:
    st.title("Raghav Handoo")
    content = """
    Highly motivated and results-driven professional with a passion for leveraging technology to drive innovation.
Having a keen interest in the field of AIML and a want to understand technology with a practical based approach, I
like to take initiatives and solve challenges along the way. Currently working on Python based projects.
In addition to my technical expertise, I am known for my strong communication skills and ability to effectively
collaborate with people from a wide range of backgrounds. I am able to work effectively with cross-functional
teams, ensuring that everyone is aligned and working towards the same goal.
    """

    st.write(content)

    st.title("Connect with me here")

