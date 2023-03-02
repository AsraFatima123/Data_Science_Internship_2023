import streamlit as st
st.title(":red[Internship] :blue[App] :green[1] :sunglasses:")
st.header(":green[basics of web app building]")
st.subheader(":pink[basic text elements]")

st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()

CODE = ''' print("Using the print statement")'''
st.code(CODE, language = 'python')