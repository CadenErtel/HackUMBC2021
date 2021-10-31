import streamlit as st
import sqlite3
from PIL import Image
from datetime import datetime

workouts = ('General Fitness', 'Push, Pull, Legs', 'HIIT', 'Marathon Prep', 'Weight Loss')
conn = sqlite3.connect('exercises.db')
cursor = conn.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS exercises (name text PRIMARY KEY, sets integer NOT NULL, reps integer NOT NULL, group text NOT NULL)')

#cursor.execute('SELECT * FROM exercises WHERE group = ?', ('leg',))

leg_group = cursor.fetchall()

class Exercise():
    
    def __init__(self, name, set, reps):
        self.name = name
        self.set = set
        self.reps = reps

    def __repr__(self):
        pass

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

    st.session_state.workout = st.sidebar.selectbox("Choose your Fitness Plan", workouts)

    # Display the selected page
    pages[page]()

def current_goals():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Weekly Fitness Plan</h1>", unsafe_allow_html=True)

    #wo_type = st.selectbox("Choose your Fitness Plan", workouts)
    sun, mon, tues, wed, thur, fri, sat = st.columns(7)

    daily_workouts = generate_workouts(st.session_state.workout)

    with sun:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Sunday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['sun']), unsafe_allow_html=True)
    with mon:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Monday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['mon']), unsafe_allow_html=True)
    with tues:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Tuesday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['tue']), unsafe_allow_html=True)
    with wed:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Wednesday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['wed']), unsafe_allow_html=True)
    with thur:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Thursday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['thur']), unsafe_allow_html=True)
    with fri:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Friday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['fri']), unsafe_allow_html=True)
    with sat:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Saturday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['sat']), unsafe_allow_html=True)

def friends():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Friends</h1>", unsafe_allow_html=True)

def calendar():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Calendar</h1>", unsafe_allow_html=True)
    dateInput = st.date_input("Which date would you like to view your fitness plan?")
    day = dateInput.weekday()
    if(day == 0):
        st.title("Monday Fitness Plan")
    elif(day == 1):
        st.title("Tuesday Fitness Plan")
    elif(day == 2):
        st.title("Wedesday Fitness Plan")
    elif(day == 3):
        st.title("Thursday Fitness Plan")
    elif(day == 4):
        st.title("Friday Fitness Plan")
    elif(day == 5):
        st.title("Saturday Fitness Plan")
    elif(day == 6):
        st.title("Sunday Fitness Plan")
    
def hands():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 34px; font-family: Andale Mono,AndaleMono,monospace;'>Health and Safety</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        #burpees_image = Image.open('Burpees.jpg')
        
        if (st.button('Burpees')):
            with st.expander("See explanation"):
                st.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'><li>This workout targets the muscles in your legs, hips, buttocks, abdomen, arms, chest, and shoulders.</li><li> dont't do a full push up</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Don't do a full push up</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Land on your heels</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Don't forget to breathe</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Stay in form</h1>", unsafe_allow_html=True)
        elif (st.button('Push ups')):
            with st.expander("See explanation"):
                st.markdown("<ul> <li>style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>This wrokout targets the chest, shoulders, and triceps and work your core, back, and legs</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Make sure your neck and spine are aligned</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Bring your hands towards your toes</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Don’t let gravity do the work for you</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>Have a strong grip on the floor</h1>", unsafe_allow_html=True)
        elif (st.button('Pull ups')):
            with st.expander("See explanation"):
                st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>This workout targets the back muscles. </h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: burgundy; font-size: 16px; font-family: Andale Mono,AndaleMono,monospace;'>Move slowly upward until your chin is above the bar, then equally slowly downward until your arms are extended again.</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: orange; font-size: 16px; font-family: Andale Mono,AndaleMono,monospace;'>Keep your shoulders back and your core engaged throughout. Then pull up. Focus on enlisting every upper body muscle to aid your upward endeavours.</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: magenta; font-size: 16px; font-family: Andale Mono,AndaleMono,monospace;'>Have a strong grip on the floor</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: left; color: yellow; font-size: 16px; font-family: Andale Mono,AndaleMono,monospace;'>Have a strong grip on the floor</h1>", unsafe_allow_html=True)
        elif (st.button('Squats')):
            st.markdown("<h1 style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>this workout targets quadriceps, hamstrings, glutes, abdominals, calves</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: left; color: white; font-size: 16px; font-family: Andale Mono,AndaleMono,monospace;'>Move slowly upward until your chin is above the bar, then equally slowly downward until your arms are extended again.</h1>", unsafe_allow_html=True)
            li

            
            
            
        #with open('Burpees.jpg', 'r') as pic:
        #st.image(Burpees.jpg)

        # if (burpees_image):
        #     st.image(burpees_image)
        # else:
        #     st.title('You suck')
        # pass

def generate_workouts(workout_type):
    days = {'sun':'', 'mon':'', 'tue':'', 'wed':'', 'thur':'', 'fri':'', 'sat':'',}
    if workout_type == workouts[0]: # General Fitness
        days['sun'] = 'Legs'
        days['mon'] = 'Rest'
        days['tue'] = 'Back'
        days['wed'] = 'Run'
        days['thur'] = 'Biceps'
        days['fri'] = 'Rest'
        days['sat'] = 'Triceps'
    elif workout_type == workouts[1]: # Push Pull Legs
        days['sun'] = 'Rest'
        days['mon'] = 'Bench Press'
        days['tue'] = 'Deadlift'
        days['wed'] = 'Squat'
        days['thur'] = 'Bench Press'
        days['fri'] = 'Deadlift'
        days['sat'] = 'Squat'
    elif workout_type == workouts[2]: # HIIT
        days['sun'] = 'Sprints'
        days['mon'] = 'Abs'
        days['tue'] = 'Chest'
        days['wed'] = 'Calves'
        days['thur'] = 'Hamstrings'
        days['fri'] = 'Sprints'
        days['sat'] = 'Abs'
    elif workout_type == workouts[3]: # Marathon Prep
        days['sun'] = 'Run'
        days['mon'] = 'Run'
        days['tue'] = 'Run'
        days['wed'] = 'Run'
        days['thur'] = 'Run'
        days['fri'] = 'Run'
        days['sat'] = 'Run'
    elif workout_type == workouts[4]: # Weight Loss
        days['sun'] = 'Sprints'
        days['mon'] = 'Abs'
        days['tue'] = 'Chest'
        days['wed'] = 'Calves'
        days['thur'] = 'Hamstrings'
        days['fri'] = 'Sprints'
        days['sat'] = 'Abs'

    return days

def string_to_p(string):
    return "<h1 style='text-align: center; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>" + string + "</h1>"

if __name__ == "__main__":
    home_page()