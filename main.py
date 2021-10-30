"""
Main Page for HackUMBC
Name: SizeUp
Authors: Caden Ertel, Christopher Slaughter, Adetunji Fasiku
Discription:
"""
import streamlit as st


st.title('SizeUp!')
st.subheader('A personal fitness community at your fingertips')


col1, col2, col3 = st.columns(3)

# this will put a button in the middle column
with col1:
    st.button('Login')

with col3:
    st.button('Create an Account')
