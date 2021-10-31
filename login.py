"""
Main Page for HackUMBC
Name: SizeUp
Authors: Caden Ertel, Christopher Slaughter, Adetunji Fasiku
Description:
"""
import streamlit as st

########################### LOGIN PAGE #######################################

def login_page() -> None:
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>SizeUp!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>A personal fitness community at your fingertips</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # this will put a button in the middle column
    with col2:
        
        st.markdown("<h1 style='text-align: center; color: white;'>SizeUp!</h1>", unsafe_allow_html=True)
        """\n"""
        usernameInput = st.text_input('Phone number, username, or email')
        passwordInput = st.text_input('Password', type="password")
        if st.button("Login"):
            if usernameInput == 'Caden' and passwordInput == 'password':
                return 'home'

        st.markdown("<a style='margin-left: auto; margin-right: auto; color: white;' href=\"https://www.facebook.com\" >Login with facebook</a>", unsafe_allow_html=True)
        st.markdown("<a style='margin: auto; color: white;' href=\"https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0\" >Forgot Password?</a>", unsafe_allow_html=True)

if __name__ == '__main__':
    login_page()