import streamlit as st

st.title("Alphanum")

a = st.text_input(label="Enter the term number (n)")

if st.button("Submit"):
    if a.isalnum():
        st.write("Yes")
    else:
        st.write("No")
        