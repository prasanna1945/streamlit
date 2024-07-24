import streamlit as st

st.set_page_config(page_icon= "💕" , page_title="Prasanna's portfolio" ,layout="wide" )

st.title("Naga Prasanna Gara" , anchor=False)

st.subheader("Frontend Web Developer")

with st.container(border=True):
    st.info("I am.......")
col1,col2,col3 = st.columns(3)

with col1:
    st.image(image="prasanna.jpeg" , width=100)
    with st.expander(label="Know me more" , expanded= False , icon = "⏬"):
        st.write("hi")