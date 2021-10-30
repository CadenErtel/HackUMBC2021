import streamlit as st
from PIL import Image

workouts = ('General Fitness', 'Push, Pull, Legs', 'HIIT', 'Marathon Prep', 'Weight Loss')

def home_page():
    
    st.set_page_config(layout="wide")

    pages = {
        "Weekly Fitness Plan": current_goals,
        "Calendar": calendar,
        "Friends": friends,
        "Health and Safety": hands
    }

    st.sidebar.title("Select a Page")
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))

    # Display the selected page
    pages[page]()

def current_goals():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Weekly Fitness Plan</h1>", unsafe_allow_html=True)

    wo_type = st.selectbox("Choose your Fitness Plan", workouts)
    sun, mon, tues, wed, thur, fri, sat = st.columns(7)

    daily_workouts = generate_workouts(wo_type)

    with sun:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Sunday</h1>", unsafe_allow_html=True)
    with mon:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Monday</h1>", unsafe_allow_html=True)
    with tues:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Tuesday</h1>", unsafe_allow_html=True)
    with wed:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Wednesday</h1>", unsafe_allow_html=True)
    with thur:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Thursday</h1>", unsafe_allow_html=True)
    with fri:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Friday</h1>", unsafe_allow_html=True)
    with sat:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Saturday</h1>", unsafe_allow_html=True)

def friends():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Friends</h1>", unsafe_allow_html=True)

def calendar():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Calendar</h1>", unsafe_allow_html=True)

def hands():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Health and Safety</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        
        st.subheader('Burpees') 
        pass

def generate_workouts(workout_type):
    days = {'sun':'', 'mon':'', 'tue':'', 'wed':'', 'thur':'', 'fri':'', 'sat':'',}
    if workout_type == 'General Fitness':
        
    

if __name__ == "__main__":
    home_page()