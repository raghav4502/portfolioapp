import streamlit as st
from Send_email import send_email

st.set_page_config(layout="wide")
st.title("Contact Me")



with st.form(key="userform"):
    user_email = st.text_input("Your email address")
    msg = st.text_area("Your message")
    msg = msg + '\n' + user_email
    button = st.form_submit_button()
    print(button)
    if button:
        send_email(msg)
        st.info("Your message was sent successfully")


