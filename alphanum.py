#check whether string contains both alphabets and numbers

import streamlit as st

st.title("Alphanum")

st.subheader("Check whether string contains both alphabets , numbers but not special characters")

a = st.text_input(label="Enter the string : ")

if st.button("Submit"):
    if  not a.isnumeric() or a.isalpha():
        for i in a:
            if ord(i.lower()) in range(97,123):
                st.write("Yes")
                break
            else:
                st.write("No")
                break
    else:
        st.write("No")
